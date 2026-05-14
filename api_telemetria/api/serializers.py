from rest_framework import serializers
from api_telemetria import models

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Veiculo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador do Veículo'},
            'descricao': {'help_text': 'Descrição do Veículo'},
            'marca': {'help_text': 'Marca do Veículo'},
            'modelo': {'help_text': 'Modelo do Veículo'},
            'ano': {'help_text': 'Ano do Veículo'},
            'horimetro': {'help_text': 'Horímetro do Veículo'},
        }

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marca
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da Marca'},
            'nome': {'help_text': 'Nome da Marca'},
        }
        
class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modelo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador do Modelo'},
            'nome': {'help_text': 'Nome do Modelo'},
        }

class MedicaoVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicaoVeiculo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da Medição do Veículo'},
            'veiculo': {'help_text': 'Identificador do Veículo associado à medição. Buscar no GET da API veículo.'},
            'medicao': {'help_text': 'Identificador do Tipo de Medição associada à medição. Buscar no GET da API medição.'},
            'data': {'help_text': 'Data e hora da medição realizada. Esta informação deve vir da automação'},
            'valor': {'help_text': 'Valor da medição realizada.'},
        }
        
class MedicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medicao
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador do Tipo de Medição'},
            'tipo': {'help_text': 'Tipo da Medição (Ex: Temperatura, Pressão, etc)'},
            'unidade_medida': {'help_text': 'Identificador da Unidade de Medida associada à medição. Buscar no GET da API unidade-medida.'},
        }

class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UnidadeMedida
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da Unidade de Medida'},
            'nome': {'help_text': 'Nome da Unidade de Medida (Ex: °C, Bar, etc)'},
        }

class UploadCSVSerializer(serializers.Serializer):
    arquivo = serializers.FileField()

    def validate_arquivo(self, value):
        if not value.name.lower().endswith(".csv"):
            raise serializers.ValidationError("O arquivo enviado deve ser um CSV.")
        return value


class MedicaoVeiculoTempSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicaoVeiculoTemp
        fields = "__all__"
        extra_kwargs = {
            'id': {'help_text': 'Identificador temporário da medição'},
            'veiculo_id': {'help_text': 'ID do veículo associado'},
            'medicao_id': {'help_text': 'ID da medição associada'},
            'data': {'help_text': 'Data e hora da medição'},
            'valor': {'help_text': 'Valor da medição'},
            'arquivo_id': {'help_text': 'Identificador do arquivo de origem'},
        }

class DadosRelatorioSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    data = serializers.DateTimeField()
    descricao = serializers.CharField()
    modelo = serializers.CharField()
    marca = serializers.CharField()
    tipo = serializers.CharField()
    valor = serializers.DecimalField(max_digits=10, decimal_places=2)