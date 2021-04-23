from django.db import models

# Create your models here.


class Funcionario(models.Model):
    objects = models.Manager()
    cpf = models.CharField(max_length=15, primary_key=True)
    nome = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    senha = models.CharField(max_length=45)
    

    
    #serve para mostrar os dados selecionados na tela de admin
    def __str__(self):
        return self.cpf

    #ordena na tela de admin os dados pelo nome em orderm alfabetica
    class Meta:
        ordering = ['nome']    