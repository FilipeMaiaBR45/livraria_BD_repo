from django.db import models

# Create your models here.


class Livro(models.Model):
    titulo = models.CharField(max_length=45, null=false)
    autor = models.CharField(max_length=45, null=false)
    editora = models.CharField(max_length=45, null=false)
    ano
    status
    preco
