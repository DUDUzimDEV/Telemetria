from django.db import models

# Create your models here.
class Marca(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Modelo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Veiculo(models.Model):
    Descricao = models.CharField(max_length=100)
    Modelo = models.ForeignKey(Modelo, on_delete=models.DO_NOTHING)
    Ano = models.DateField()
    Horimetro = models.IntegerField(max_length=30)


class MedicaoVeiculo(models.Model):
    Data = models.DateField()
    Valor = models.DecimalField(max_digits=8, decimal_places=2)

class Medicao(models.Model):
    Tipo = models.CharField(max_length=100)

class UnidadeMedida(models.Model):
    Nome = models.CharField(max_length=100)