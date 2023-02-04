from django.db import models

# Create your models here.

class bicicletas(models.Model):
    marca = models.CharField(max_length=150)
    modelo = models.CharField(max_length=150)
    tamanho = models.CharField(max_length=150)
    ano = models.IntegerField()