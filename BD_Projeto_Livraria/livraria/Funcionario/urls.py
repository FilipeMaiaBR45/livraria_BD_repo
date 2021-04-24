from django.urls import path

from . import views

app_name = "funcionario"

urlpatterns = [
    #path('listar/', views.listar_funcionarios, name='listar'),
    path('adicionar/', views.adicionar_funcionario, name='adicionar'),
   # path('deletar/<int:pk>/', views.deletar_funcionario, name="deletar"),
]