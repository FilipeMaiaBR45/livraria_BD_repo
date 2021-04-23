from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from django.db import connection
from collections import namedtuple

from django.contrib import messages

from .models import Funcionario
from .forms import FuncionarioForm


def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def listar_funcionarios(request):
    with connection.cursor() as cursor:
        # Função SQL que se quer executar (SELECT, INSERT, DELETE, UPDATE, ...)
        # Parâmetros serão passados nos []
        cursor.execute("SELECT * FROM funcionario_funcionario", [])
        # resultado = cursor.fetchall()

        # Função que permite acessar os atributos das tuplas da tabela resultante da query
        resultado = namedtuplefetchall(cursor)
    return render(request, 'templates/Funcionario/listar.html',
                  {'funcionarios': resultado}
                  )


def adicionar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():

            cpf = form.cleaned_data['cpf']
            nome = form.cleaned_data['nome']
            telefone = form.cleaned_data['telefone']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

   

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO funcionario_funcionario (cpf, nome, telefone,"
                           "email, senha)"
                           "VALUES (%s, %s, %s, %s, %s)",
                           [cpf, nome, telefone, email, senha])
            resultado = cursor.fetchall()
        return redirect('funcionario:listar')
    else:
        form = FuncionarioForm()
    return render(request, 'Funcionario/adicionar.html',
                  {'form': form}
                  )




# Create your views here.
