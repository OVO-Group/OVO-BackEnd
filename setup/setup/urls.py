from django.contrib import admin
from django.urls import path
from ovo.views import UserCreateView, UserListView, UserUpdateView, UserDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar/<int:id_usuario>', UserListView.as_view(), name='usuario_list'),
    path('cadastrar/', UserCreateView.as_view(), name='usuario_cadastro'),
    path('atualizar/<int:id_usuario>', UserUpdateView.as_view(), name='usuario_atualiza'),
    path('deletar/<int:id_usuario>', UserDeleteView.as_view(), name='usuario_deleta'),
]
