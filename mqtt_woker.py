import datetime
import os
import json
import django
import paho.mqtt.client as mqtt
from django.utils import timezone

# inicializa o Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from django.conf import settings
from api_telemetria.models import MedicaoVeiculo, Veiculo, Medicao


def inserir_medicao(veiculo_id, medicao_id, valor, datae):
    """
    Função para inserir uma medição no banco de dados.
    """
    try:
        veiculo = Veiculo.objects.get(id=veiculo_id)
        medicao = Medicao.objects.get(id=medicao_id)
        
        # Tornar o datetime aware se necessário
        if timezone.is_naive(datae):
            datae = timezone.make_aware(datae)
        
        MedicaoVeiculo.objects.create(
            data=datae,
            veiculo=veiculo,
            medicao=medicao,
            valor=valor,
        )
        
        print(f"[MQTT] Salvo: veiculo={veiculo_id} medicao={medicao_id} valor={valor} data={datae}")
        return True
    except Veiculo.DoesNotExist:
        print(f"[ERRO] Veículo com ID {veiculo_id} não encontrado.")
        return False
    except Medicao.DoesNotExist:
        print(f"[ERRO] Medição com ID {medicao_id} não encontrada.")
        return False
    except Exception as e:
        print(f"[ERRO] Falha ao inserir medição: {e}")
        return False


def on_connect(client, userdata, flags, reason_code, properties=None):
    print(f"[MQTT] Conectado com rc={reason_code}")

    topic = settings.MQTT.get("TOPIC", "planta/sensores/#")
    client.subscribe(topic)
    print(f"[MQTT] Inscrito em {topic}")


def get_field(obj, *keys):
    for key in keys:
        if key in obj:
            return obj[key]
    raise KeyError(f"Nenhum dos campos {keys} encontrado em {obj}")


def parse_medicao_item(item):
    valor = float(get_field(item, "valor", "value"))
    veiculo_id = int(get_field(item, "veiculoid", "veiculo_id", "vehicleId"))
    medicao_id = int(get_field(item, "sensorid", "medicaoid", "medicao_id", "sensor_id"))
    data_raw = get_field(item, "data", "timestamp", "datetime")
    datae = datetime.datetime.fromisoformat(data_raw)
    return veiculo_id, medicao_id, valor, datae


def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        data = json.loads(payload)
        print(f"[MQTT] Mensagem recebida: {data}")

        if isinstance(data, list):
            for item in data:
                veiculo_id, medicao_id, valor, datae = parse_medicao_item(item)
                inserir_medicao(veiculo_id, medicao_id, valor, datae)
        else:
            veiculo_id, medicao_id, valor, datae = parse_medicao_item(data)
            inserir_medicao(veiculo_id, medicao_id, valor, datae)

    except KeyError as e:
        print(f"[ERRO] Falha ao processar mensagem: {e}")
    except ValueError as e:
        print(f"[ERRO] Falha ao converter valores da mensagem: {e}")
    except json.JSONDecodeError as e:
        print(f"[ERRO] Payload MQTT inválido: {e}")
    except Exception as e:
        print(f"[ERRO] Falha ao processar mensagem: {e}")


def main():
    mqtt_cfg = settings.MQTT

    host = mqtt_cfg.get("HOST", "127.0.0.1")
    port = mqtt_cfg.get("PORT", 1883)
    user = mqtt_cfg.get("USERNAME")
    password = mqtt_cfg.get("PASSWORD")

    # Atualizar para a versão mais recente da API de callback
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

    # >>> usuário e senha vindos do settings <<<
    if user and password:
        client.username_pw_set(user, password)

    client.on_connect = on_connect
    client.on_message = on_message

    print(f"[MQTT] Conectando em {host}:{port}…")
    client.connect(host, port, 60)

    client.loop_forever()


if __name__ == "__main__":
    main()