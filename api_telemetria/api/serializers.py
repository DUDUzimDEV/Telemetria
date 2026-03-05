from rest_framework import serializers
from api_telemetria import models

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Veiculo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador do Veículo'},
            'Descricao': {'help_text': 'Descrição do Veículo'},
            'Marca': {'help_text': 'Marca do Veículo'},
            'Modelo': {'help_text': 'Modelo do Veículo'},
            'Ano': {'help_text': 'Ano do Veículo'},
            'Horimetro': {'help_text': 'Horímetro do Veículo'},
        }

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marca
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da Marca'},
            'Nome': {'help_text': 'Nome da Marca'},
        }
        
class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modelo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador do Modelo'},
            'Nome': {'help_text': 'Nome do Modelo'},
        }

class MedicaoVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicaoVeiculo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da Medição do Veículo'},
            'Veiculo': {'help_text': 'Identificador do Veículo associado à medição. Buscar no GET da API veículo.'},
            'Medicao': {'help_text': 'Identificador do Tipo de Medição associada à medição. Buscar no GET da API medição.'},
            'Data': {'help_text': 'Data e hora da medição realizada. Esta informação deve vir da automação'},
            'Valor': {'help_text': 'Valor da medição realizada.'},
        }
        
class MedicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medicao
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador do Tipo de Medição'},
            'Tipo': {'help_text': 'Tipo da Medição (Ex: Temperatura, Pressão, etc)'},
            'UnidadeMedida': {'help_text': 'Identificador da Unidade de Medida associada à medição. Buscar no GET da API unidade-medida.'},
        }

class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UnidadeMedida
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da Unidade de Medida'},
            'Nome': {'help_text': 'Nome da Unidade de Medida (Ex: °C, Bar, etc)'},
        }