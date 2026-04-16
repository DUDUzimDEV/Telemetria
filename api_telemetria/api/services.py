# Importações de bibliotecas padrão do Python
import csv              # Para leitura de arquivos CSV
import os               # Para manipulação de diretórios e caminhos
import uuid             # Para gerar identificadores únicos
from decimal import Decimal   # Para trabalhar com números decimais com precisão
from datetime import datetime # Para manipulação e conversão de datas

# Importações do Django
from django.conf import settings                     # Acessa configurações do projeto
from django.core.files.storage import FileSystemStorage # Para salvar arquivos no sistema
from django.db import transaction, connection        # Para transações e conexão com o banco

# Importação dos modelos da aplicação
from api_telemetria.models import MedicaoVeiculoTemp, Veiculo, Medicao


# Função que executa uma stored procedure no banco de dados
def executar_procedure_pos_importacao(arquivoid):
    """
    Executa a procedure no banco.
    Ajuste o nome da procedure e os parâmetros conforme sua necessidade.
    """
    with connection.cursor() as cursor:
        # Exemplo sem parâmetro:
        # cursor.callproc("sua_procedure")

        # Exemplo passando arquivoid:
        cursor.callproc("processa_arquivo", [arquivoid])


# Função principal que processa o CSV de medições
def processar_csv_medicoes(arquivo):
    # Gera um identificador único para essa importação
    arquivoid = str(uuid.uuid4())

    # Define a pasta de destino dentro do MEDIA_ROOT
    pasta_destino = os.path.join(settings.MEDIA_ROOT, "importacoes_medicao")
    os.makedirs(pasta_destino, exist_ok=True)  # Cria a pasta se não existir

    # Define o nome do arquivo salvo (UUID + nome original)
    nome_salvo = f"{arquivoid}_{arquivo.name}"
    fs = FileSystemStorage(location=pasta_destino)
    nome_arquivo_salvo = fs.save(nome_salvo, arquivo)  # Salva o arquivo
    caminho_completo = os.path.join(pasta_destino, nome_arquivo_salvo)

    # Variáveis de controle
    total_linhas_arquivo = 0
    erros = []                # Lista para armazenar erros encontrados
    linhas_para_inserir = []  # Lista de objetos a serem inseridos no banco

    # Cache de veículos e medições já existentes no banco
    veiculos_cache = {v.id: v for v in Veiculo.objects.all()}
    medicoes_cache = {m.id: m for m in Medicao.objects.all()}

    # Abre o arquivo CSV para leitura
    with open(caminho_completo, mode="r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter=';')  # Lê cada linha como dicionário

        # Define os campos obrigatórios
        campos_esperados = {"veiculoid", "medicaoid", "data", "valor"}

        # Valida se existe cabeçalho
        if not reader.fieldnames:
            raise Exception("O CSV não possui cabeçalho.")

        # Valida se os campos esperados estão presentes
        if not campos_esperados.issubset(set(reader.fieldnames)):
            raise Exception(
                f"Cabeçalho inválido. Esperado: {list(campos_esperados)}. Recebido: {reader.fieldnames}"
            )

        # Itera sobre cada linha do CSV
        for numero_linha, row in enumerate(reader, start=2):  # começa em 2 (linha após cabeçalho)
            total_linhas_arquivo += 1

            try:
                # Converte IDs para inteiro
                id_veiculo = int(row["veiculoid"])
                id_medicao = int(row["medicaoid"])

                # Valida se veículo existe
                veiculo = veiculos_cache.get(id_veiculo)
                if not veiculo:
                    raise Exception(f"Veículo {id_veiculo} não encontrado.")

                # Valida se medição existe
                medicao = medicoes_cache.get(id_medicao)
                if not medicao:
                    raise Exception(f"Medição {id_medicao} não encontrada.")

                # Converte data e valor
                data_convertida = datetime.strptime(
                    row["data"].strip(),
                    "%Y-%m-%d %H:%M:%S"
                )
                valor_convertido = Decimal(row["valor"].strip())

                # Cria objeto temporário para inserção
                linhas_para_inserir.append(
                    MedicaoVeiculoTemp(
                        veiculoid=veiculo,
                        medicaoid=medicao,
                        data=data_convertida,
                        valor=valor_convertido,
                        arquivoid=arquivoid
                    )
                )

            except Exception as e:
                # Se houver erro, registra a linha e a mensagem
                erros.append({
                    "linha": numero_linha,
                    "erro": str(e)
                })

    # Conta quantas linhas válidas foram preparadas
    total_linhas_validas = len(linhas_para_inserir)

    # Inicia transação para garantir consistência
    with transaction.atomic():
        if linhas_para_inserir:
            # Insere em lote para maior eficiência
            MedicaoVeiculoTemp.objects.bulk_create(linhas_para_inserir, batch_size=1000)

        # Conta quantas linhas foram realmente inseridas
        total_linhas_importadas = MedicaoVeiculoTemp.objects.filter(
            arquivoid=arquivoid
        ).count()

        # Confere se quantidade bate
        quantidades_conferem = total_linhas_validas == total_linhas_importadas

        if quantidades_conferem:
            # Se tudo certo, executa procedure
            executar_procedure_pos_importacao(arquivoid)
        else:
            # Se houve falha, apaga os dados inseridos
            MedicaoVeiculoTemp.objects.filter(arquivoid=arquivoid).delete()

    # Retorna resumo da importação
    return {
        "arquivoid": arquivoid,
        "arquivo_salvo": nome_arquivo_salvo,
        "caminho": caminho_completo,
        "total_linhas_arquivo": total_linhas_arquivo,
        "total_linhas_importadas": total_linhas_importadas,
        "quantidades_conferem": total_linhas_validas == total_linhas_importadas,
        "erros": erros
    }
