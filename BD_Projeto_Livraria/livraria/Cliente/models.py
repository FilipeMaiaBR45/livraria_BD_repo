from django.db import models

# Create your models here.

class Cliente(models.Model):
    cpf = models.CharField(max_length=14, primary_key=True)
    nome = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45)
    email = models.CharField(max_length=45, unique=True)
    senha =  models.CharField(max_length=45)

    