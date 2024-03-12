from django.contrib import admin
from django.urls import path
from ovo.views import UserCreateView, UserListView, UserUpdateView, UserDeleteView, EnderecoListView, EnderecoCreateView, EnderecoUpdateView, EnderecoDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar/<int:id_usuario>', UserListView.as_view(), name='usuario_list'),
    path('cadastrar/', UserCreateView.as_view(), name='usuario_cadastro'),
    path('atualizar/<int:id_usuario>', UserUpdateView.as_view(), name='usuario_atualiza'),
    path('deletar/<int:id_usuario>', UserDeleteView.as_view(), name='usuario_deleta'),
    path('listar/endereco/<int:id_endereco>', EnderecoListView.as_view(), name='endereco_list'),
    path('cadastrar/endereco/', EnderecoCreateView.as_view(), name='endereco_cadastro'),
    path('atualizar/endereco/<int:id_endereco>', EnderecoUpdateView.as_view(), name='endereco_atualiza'),
    path('deletar/endereco/<int:id_endereco>', EnderecoDeleteView.as_view(), name='endereco_deleta')
]