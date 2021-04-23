from django.db import models

# Create your models here.

from Funcionario.models import Funcionario
class Livro(models.Model):
     objects = models.Manager()
     titulo = models.CharField(max_length=45)
     autor = models.CharField(max_length=45)
     editora = models.CharField(max_length=45)
     ano = models.IntegerField()
     preco = models.IntegerField()
     quantidade = models.IntegerField(default=0)
     funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
     
      
