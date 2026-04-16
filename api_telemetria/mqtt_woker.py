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


def on_connect(client, userdata, flags, rc):
    print(f"[MQTT] Conectado com rc={rc}")

    topic = settings.MQTT.get("TOPIC", "planta/sensores/#")
    client.subscribe(topic)
    print(f"[MQTT] Inscrito em {topic}")


def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())

        valor = float(data["valor"])
        veiculo_id = int(data["veiculoid"])
        medicao_id = int(data["sensorid"])
        datae = datetime.datetime.fromisoformat(data["data"])

        veiculo = Veiculo.objects.get(id=veiculo_id)
        medicao = Medicao.objects.get(id=medicao_id)
        MedicaoVeiculo.objects.create(
            data=datae,
            veiculo_id=veiculo,
            medicao_id=medicao,
            valor=valor,
        )

        print(f"[MQTT] Salvo: veiculo={veiculo_id} medicao={medicao_id} valor={valor}")

    except Exception as e:
        print(f"[ERRO] Falha ao processar mensagem: {e}")


def main():
    mqtt_cfg = settings.MQTT

    host = mqtt_cfg.get("HOST", "127.0.0.1")
    port = mqtt_cfg.get("PORT", 1883)
    user = mqtt_cfg.get("USERNAME")
    password = mqtt_cfg.get("PASSWORD")

    client = mqtt.Client()

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