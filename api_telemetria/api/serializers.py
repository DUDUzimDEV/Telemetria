from rest_framework import serializers
from api_telemetria import models

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marca
        fields = "__all__"
        extra_kwargs = {
            'id': {'help_text': 'Identificador da Marca'},
            'nome': {'help_text': 'Nome da marca do veículo'}
        }


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Veiculo
        fields = "__all__"
        extra_kwargs = {
            'id': {'help_text': 'Identificador do Veículo'},
            'marcaid': {'help_text': 'Identificador da marca. Buscar no GET da API Marca'},
            'modeloid': {'help_text': 'Identificador do modelo. Buscar no GET da API Modelo'},
            'placa': {'help_text': 'Placa do veículo'},
            'ano': {'help_text': 'Ano de fabricação do veículo'}
        }


class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modelo
        fields = "__all__"
        extra_kwargs = {
            'id': {'help_text': 'Identificador do Modelo'},
            'marcaid': {'help_text': 'Identificador da marca. Buscar no GET da API Marca'},
            'nome': {'help_text': 'Nome do modelo do veículo'}
        }


class MedicaoVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicaoVeiculo
        fields = "__all__"
        extra_kwargs = {
            'id': {'help_text': 'Identificador da Medição do Veículo'},
            'veiculoid': {'help_text': 'Identificador do veículo. Buscar no GET da API Veiculo'},
            'medicaoid': {'help_text': 'Identificador do tipo de medição. Buscar no GET da API Medicao'},
            'data': {'help_text': 'Data e hora da medição realizada, essa informação deve vir da automação'},
            'valor': {'help_text': 'Valor medido na automação'}
        }


class MedicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medicao
        fields = "__all__"
        extra_kwargs = {
            'id': {'help_text': 'Identificador da Medição'},
            'nome': {'help_text': 'Nome do tipo de medição (ex: Horímetro, Odômetro)'},
            'unidademedidaid': {'help_text': 'Identificador da unidade de medida. Buscar no GET da API UnidadeMedida'}
        }


class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UnidadeMedida
        fields = "__all__"
        extra_kwargs = {
            'id': {'help_text': 'Identificador da Unidade de Medida'},
            'nome': {'help_text': 'Nome da unidade de medida (ex: KM, Horas, Litros)'},
            'sigla': {'help_text': 'Sigla da unidade de medida'}
        }