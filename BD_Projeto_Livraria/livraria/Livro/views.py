from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from django.db import connection
from collections import namedtuple

from django.contrib import messages

from .models import Livro
from .forms import LivroForm
from .forms import UpdateForm



def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def listar_livros(request):
    with connection.cursor() as cursor:
        # Função SQL que se quer executar (SELECT, INSERT, DELETE, UPDATE, ...)
        # Parâmetros serão passados nos []
        cursor.execute("SELECT * FROM livro_livro", [])
        # resultado = cursor.fetchall()

        # Função que permite acessar os atributos das tuplas da tabela resultante da query
        resultado = namedtuplefetchall(cursor)
    return render(request, 'Livro/listar.html',
                  {'livros': resultado}
                  )

#tenho que resolver o erro no cadastro(fazer isso com um sistema de login)
def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():

            titulo = form.cleaned_data['titulo']
            autor = form.cleaned_data['autor']
            editora = form.cleaned_data['editora']
            ano = form.cleaned_data['ano']
            preco = form.cleaned_data['preco']
            quantidade = form.cleaned_data['quantidade']
            funcionario = form.cleaned_data['funcionario']


   

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO livro_livro (titulo, autor, editora,"
                           "ano, preco, quantidade, funcionario_id)"
                           "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           [titulo, autor, editora, ano,  preco, quantidade, funcionario])
            resultado = cursor.fetchall()
        return redirect('livro:listar')
    else:
        form = LivroForm()
    return render(request, 'Livro/adicionar.html',
                  {'form': form}
                  )


def deletar_livro(request, pk):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM livro_livro WHERE id=%s", [pk])
    return redirect('livro:listar')



def editar_livro(request, pk):
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
           
            titulo_livro = form.cleaned_data['titulo']
            autor = form.cleaned_data['autor']
            editora = form.cleaned_data['editora']
            ano = form.cleaned_data['ano']
            preco = form.cleaned_data['preco']
            quantidade = form.cleaned_data['quantidade']
            #funcionario = form.cleaned_data['funcionario']


            with connection.cursor() as cursor:
                cursor.execute("UPDATE livro_livro SET titulo=%s, autor=%s, "
                               "editora=%s, ano=%s, preco=%s, quantidade=%s "
                               "WHERE id=%s",
                                [titulo_livro, autor, editora, ano, preco, quantidade, pk])
                resultado = cursor.fetchall()
            return redirect('livro:listar')
    else:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM livro_livro WHERE id=%s", [pk])
            resultado_livro = namedtuplefetchall(cursor)
        form = UpdateForm(initial={'titulo': resultado_livro[0].titulo,
                                    'autor': resultado_livro[0].autor,
                                    'editora': resultado_livro[0].editora,
                                    'ano': resultado_livro[0].ano,
                                    'preco': resultado_livro[0].preco,
                                    'quantidade': resultado_livro[0].quantidade,
                                    })
    return render(request, 'Livro/editar.html',
                {'form': form}
                )

