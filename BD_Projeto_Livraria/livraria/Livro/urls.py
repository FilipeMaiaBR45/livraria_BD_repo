from django.urls import path

from . import views

app_name = "livro"

urlpatterns = [
    path('listar/', views.listar_livros, name='listar'),
    path('adicionar/', views.adicionar_livro, name='adicionar'),
    path('deletar/<int:pk>/', views.deletar_livro, name="deletar"),
    path('editar/<int:pk>', views.editar_livro, name="editar"),
]