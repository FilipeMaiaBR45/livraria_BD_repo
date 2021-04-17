from django.db import models

# Create your models here.


class Livro(models.Model):
    titulo = models.CharField(max_length=45, null=False)
    autor = models.CharField(max_length=45, null=False)
    editora = models.CharField(max_length=45, null=False)
    ano = models.PositiveIntegerField(default = 0)
    #status models.PositiveIntegerField(default = 0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
