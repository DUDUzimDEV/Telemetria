from django.db import models

# Create your models here.

class Veiculo(models.Model):
    Descricao = models.CharField(max_length=255)
    Marca = models.ForeignKey('Marca', on_delete=models.DO_NOTHING)
    Modelo = models.ForeignKey('Modelo', on_delete=models.DO_NOTHING)
    Ano = models.IntegerField()
    Horimetro = models.IntegerField()
    
    def __str__(self):
        return f'{self.Descricao} - {self.Marca} - {self.Modelo} - {self.Ano} - {self.Horimetro}'
    
class Marca(models.Model):
    Nome = models.CharField(max_length=30)
    
    def __str__(self):
        return self.Nome

class Modelo(models.Model):
    Nome = models.CharField(max_length=30)
    
    def __str__(self):
        return self.Nome
    

class MedicaoVeiculo(models.Model):
    Veiculo = models.ForeignKey('Veiculo', on_delete=models.DO_NOTHING)
    Medicao = models.ForeignKey('Medicao', on_delete=models.DO_NOTHING)
    Data = models.DateTimeField()
    Valor = models.FloatField()
    
    def __str__(self):
        return f"{self.Veiculo} - {self.Medicao}"
    
class Medicao(models.Model):
    Tipo = models.CharField(max_length=30)
    UnidadeMedida = models.ForeignKey('UnidadeMedida', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.Tipo} - {self.UnidadeMedida}"

class UnidadeMedida(models.Model):
    Nome = models.CharField(max_length=30)
    
    def __str__(self):
        return self.Nome


    
    