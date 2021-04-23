from django import forms
from django.db import connection

from django.contrib import messages

from django.core.exceptions import ValidationError

from .models import Livro


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'editora', 'ano',
                  'preco', 'quantidade', 'funcionario']

    def clean(self):
        cleaned_data = super().clean()
        # Pega o nome que foi adicionado no formulário
        titulo = cleaned_data.get("titulo")
        autor = cleaned_data.get("autor")
        editora = cleaned_data.get("editora")
        ano = cleaned_data.get("ano")

        # Seleciona se há produtos com este mesmo nome
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM livro_livro WHERE titulo=%s and autor=%s and editora=%s and ano=%s", [titulo, autor, editora, ano])
            resultado_livro = cursor.fetchall()

        # Se a lista não foi vazia, há produto com o mesmo nome
        if (len(resultado_livro) != 0):
            raise ValidationError("livro já cadastradado.")


class UpdateForm(forms.ModelForm):
    class Meta:
       model = Livro
       fields = ['titulo', 'autor', 'editora', 'ano',
                  'preco', 'quantidade']

    def clean(self):
        cleaned_data = super().clean()
        # Pega o nome que foi adicionado no formulário
        titulo = cleaned_data.get("titulo")

        # Seleciona se há animals com este mesmo nome
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM livro_livro WHERE titulo=%s", [titulo])
            resultado_titulo = cursor.fetchall()

        if (len(resultado_titulo) != 0):
            raise ValidationError("livro já cadastradado.")
