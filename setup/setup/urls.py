from django.contrib import admin
from django.urls import path
from ovo.views import UserCreateView, UserListView, UserUpdateView, UserDeleteView,\
    EnderecoListView, EnderecoCreateView, EnderecoUpdateView, EnderecoDeleteView,\
    LoginCelularView, LoginEmailView ,EnderecoUsuarioListView, RestauranteListView,\
    ProdutoListView, VerificaCodigo, VerificaEmail,\
    ProdutoListView, VerificaCodigo, GetRestauranteView, RestauranteCreateView,\
    RestauranteDeleteView, RestauranteEditView, ProdutoCreateView, ProdutoDeleteView,\
    ProdutoEditView, GetProdutoView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
#rotas para gerar token jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#Admin
    path('admin/', admin.site.urls),
#listar usuário por id usuário
    path('listar/<int:id_usuario>', UserListView.as_view(), name='usuario_list'),
#cadastrar usuário
    path('cadastrar/', UserCreateView.as_view(), name='usuario_cadastro'),
#atualizar usuário por id usuário
    path('atualizar/<int:id_usuario>', UserUpdateView.as_view(), name='usuario_atualiza'),
#deletar usuário por id usuário
    path('deletar/<int:id_usuario>', UserDeleteView.as_view(), name='usuario_deleta'),
#listar endereço por id endereço
    #path('listar/endereco/<int:id_endereco>', EnderecoListView.as_view(), name='endereco_list'),
#listar endereço por id usuário
    path('listar/endereco-usuario/<int:id_usuario>', EnderecoUsuarioListView.as_view(), name='endereco_usuario_list'),
#cadastrar endereco
    path('cadastrar/endereco/', EnderecoCreateView.as_view(), name='endereco_cadastro'),
#atualizar endereco por id endereco
    path('atualizar/endereco/<int:id_endereco>', EnderecoUpdateView.as_view(), name='endereco_atualiza'),
#deletar endereco por id endereco
    path('deletar/endereco/<int:id_endereco>', EnderecoDeleteView.as_view(), name='endereco_deleta'),
#login por email
    path('login/email', LoginEmailView.as_view(), name='login_email'),
#login por celular
    path('login/celular', LoginCelularView.as_view(), name='login_celular'),
#listar restaurantes
    path('restaurante/', RestauranteListView.as_view(), name='restaurante'),
#Listar um restaurante específico
    path('restaurante/<int:id_restaurante>', GetRestauranteView.as_view(), name='get_restaurante'),
#criar restaurantes
    path('restaurante/criar', RestauranteCreateView.as_view(), name='Criar_restaurante'),
#Deletar restaurantes
    path('restaurante/deletar/<int:id_restaurante>', RestauranteDeleteView.as_view(), name="Deletar_restaurante"), 
#Editar restaurante
    path('restaurante/editar/<int:id_restaurante>', RestauranteEditView.as_view(), name='Editar_restaurante'),
#listar produtos
    path('produtos/<int:id_restaurante>', ProdutoListView.as_view(), name='produtos'),
#listar um produto específico
    path('produto/<int:id_produto>', GetProdutoView.as_view(), name='get_produto'),
#criar produtos
    path('produto/criar', ProdutoCreateView.as_view(), name='Criar_produto'),
#Deletar produtos
    path('produto/deletar/<int:id_produto>', ProdutoDeleteView.as_view(), name="Deletar_produto"), 
#editar produtos
    path('produto/editar/<int:id_produto>', ProdutoEditView.as_view(), name='Editar_produto'),
#verificar codigo do email    
    path('login/verificacao', VerificaCodigo.as_view(), name='verifica_codigo'),

    path('verifica/email', VerificaEmail.as_view(), name='verifica_email'),
    path('login/verificacao', VerificaCodigo.as_view(), name='verifica_codigo'),
]


