from rest_framework import viewsets
from api_telemetria import models
from api_telemetria.api import serializers
from drf_yasg.utils import swagger_auto_schema

class MarcaViewset(viewsets.ModelViewSet):
    serializer_class = serializers.MarcaSerializer
    queryset = models.Marca.objects.all()
    @swagger_auto_schema(
        operation_description="Retorna todas as marcas",
        responses={200: serializers.MarcaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de marca",
        responses={201: serializers.MarcaSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de marca conforme ID informado",
        responses={200: serializers.MarcaSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera a marca conforme dados passados, para o ID informado",
        responses={200: serializers.MarcaSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta a marca conforme o ID passado",
        responses={200: serializers.MarcaSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class VeiculoViewset(viewsets.ModelViewSet):
    serializer_class = serializers.VeiculoSerializer
    queryset = models.Veiculo.objects.all()
    @swagger_auto_schema(
        operation_description="Retorna todos os veiculos",
        responses={200: serializers.VeiculoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de veiculo",
        responses={201: serializers.VeiculoSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de veiculo conforme ID informado",
        responses={200: serializers.VeiculoSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o veiculo conforme dados passados, para o ID informado",
        responses={200: serializers.VeiculoSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta o veiculo conforme o ID passado",
        responses={200: serializers.VeiculoSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ModeloViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ModeloSerializer
    queryset = models.Modelo.objects.all()
    @swagger_auto_schema(
        operation_description="Retorna todos os modelos",
        responses={200: serializers.ModeloSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de modelo",
        responses={201: serializers.ModeloSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de modelos de veiculo conforme ID informado",
        responses={200: serializers.ModeloSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o modelo conforme dados passados, para o ID informado",
        responses={200: serializers.ModeloSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta o modelo conforme o ID passado",
        responses={200: serializers.ModeloSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class MedicaoVeiculoViewset(viewsets.ModelViewSet):
    serializer_class = serializers.MedicaoVeiculoSerializer
    queryset = models.MedicaoVeiculo.objects.all()
    @swagger_auto_schema(
        operation_description="Retorna todas as Medições de Veiculo",
        responses={200: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de tipo de Unidade de Medida",
        responses={201: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro das medições do veiculo conforme ID informado",
        responses={200: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera a medição do veiculo conforme dados passados, para o ID informado",
        responses={200: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta a Medição do veiculo conforme o ID passado",
        responses={200: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class MedicaoViewset(viewsets.ModelViewSet):
    serializer_class = serializers.MedicaoSerializer
    queryset = models.Medicao.objects.all()
    @swagger_auto_schema(
        operation_description="Retorna todas as informações de tipos de medição",
        responses={200: serializers.MedicaoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de tipo de medição",
        responses={201: serializers.MedicaoSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de tipo de medição conforme  ID informado",
        responses={200: serializers.MedicaoSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o tipo de medição conforme dados passados, para o ID informado",
        responses={200: serializers.MedicaoSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta a medição conforme o ID passado",
        responses={200: serializers.MedicaoSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class UnidadeMedidaViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UnidadeMedidaSerializer
    queryset = models.UnidadeMedida.objects.all()
    @swagger_auto_schema(
        operation_description="Retorna todos os tipos de Unidade de Medida",
        responses={200: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de Unidade de Medida",
        responses={201: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de unidade de medida conforme ID informado",
        responses={200: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o tipo de unidade de medida conforme dados passados, para o ID informado",
        responses={200: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta a categoria conforme o ID passado",
        responses={200: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)