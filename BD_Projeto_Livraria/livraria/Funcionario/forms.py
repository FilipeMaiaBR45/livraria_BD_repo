from django import forms
from django.db import connection

from django.core.exceptions import ValidationError

from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['cpf', 'nome', 'telefone', 'email',
                    'senha']
    
    def clean(self):
        cleaned_data = super().clean()
        # Pega o nome que foi adicionado no formulário
        cpf = cleaned_data.get("cpf") 

        # Seleciona se há produtos com este mesmo nome
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM funcionario_funcionario WHERE cpf=%s", [cpf])
            resultado_funcionario = cursor.fetchall()
        
        # Se a lista não foi vazia, há produto com o mesmo nome
        if (len(resultado_funcionario) != 0):
            raise ValidationError("Já foi criado um produto com este nome. Escolha outro nome.")


