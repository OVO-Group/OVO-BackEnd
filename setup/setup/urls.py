from django.contrib import admin
from django.urls import path
from ovo.views import PedidoCreateView

from ovo.views import UserCreateView, UserListView, UserUpdateView, UserDeleteView,\
    EnderecoUsuarioListView, EnderecoRestauranteListView, EnderecoCreateView, EnderecoUpdateView, EnderecoDeleteView,\
    LoginCelularView, LoginEmailView, RestauranteListView,\
    ProdutoListView, VerificaCodigo, VerificaEmail,\
    ProdutoListView, VerificaCodigo, GetRestauranteView, RestauranteCreateView,\
    RestauranteDeleteView, RestauranteEditView, ProdutoCreateView, ProdutoDeleteView,\
    ProdutoEditView, GetProdutoView, ComandaListView, ComandaCreateView, ComandaUpdateView,\
    ComandaDeleteView, TipoPagamentoListView, TipoPagamentoCreateVIew, TipoPagamentoUpdateView,\
    TipoPagamentoDeleteView, PedidoListView, PedidoCreateView, PedidoUpdateView, PedidoDeleteView,\
    GetEnderecoView, TipoEntregaListView, BuscaView, ProdutoListAll, RelatorioTotalPagoPedidoView,\
    PedidosAbertosRestaurante, EnviaEmailView, RelatorioTipoPagamento,\
    GetEnderecoView, TipoEntregaListView, BuscaView, PedidosAbertosRestaurante, ProdutoListAll, RelatorioTotalPagoPedidoView, EnviaEmailView,\
    GetEnderecoView, TipoEntregaListView, BuscaView, ProdutoListAll, RelatorioTotalPagoPedidoView, CartaoListView, CartaoUsuarioListView, CartaoCreateView, CartaoDeleteView, CartaoUpdateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('pedido/criar', PedidoCreateView.as_view(), name='criar_pedido'),
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
    path('endereco/<int:id_endereco>', GetEnderecoView.as_view(), name='get_endereco'),
#listar endereço por id restaurante
    path('endereco-restaurante/<int:id_restaurante>', EnderecoRestauranteListView.as_view(), name='endereco_list'),
#listar endereço por id usuário
    path('endereco-usuario/<int:id_usuario>', EnderecoUsuarioListView.as_view(), name='endereco_list'),
#cadastrar endereco
    path('cadastrar/endereco', EnderecoCreateView.as_view(), name='endereco_cadastro'),
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
#listar todos os produtos 
    path('produtos/todos', ProdutoListAll.as_view(), name='produtos_todos'),
#listar produtos por id do restaurante
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
#verificação de email
    path('verifica/email', VerificaEmail.as_view(), name='verifica_email'),
#verificação de login
    path('login/verificacao', VerificaCodigo.as_view(), name='verifica_codigo'),

    #path('comanda/<id_comanda>', ComandaListView.as_view(), name='comanda'),

    path('comanda/criar', ComandaCreateView.as_view(), name='cria_comanda'),

    #path('comanda/editar/<id_comanda>', ComandaUpdateView.as_view(), name='edita_comanda'),

    #path('comanda/deletar/<id_comanda>', ComandaDeleteView.as_view(), name='deleta_comanda'),

    path('tipo_pagamento/', TipoPagamentoListView.as_view(), name='tipo_pagamento'),

    path('tipo_pagamento/criar', TipoPagamentoCreateVIew.as_view(), name='criar_tipo_pagamento'),

    path('tipo_pagamento/editar/<id_tipo_pagamento>', TipoPagamentoUpdateView.as_view(), name='editar_tipo_pagamento'),

    path('tipo_pagamento/deletar/<id_tipo_pagamento>', TipoPagamentoDeleteView.as_view(), name='deletar_tipo_pagamento'),

    path('pedido/<id_produto>', PedidoListView.as_view(), name='pedido'),

   

    path('concluir/<int:id_pedido>', PedidoUpdateView.as_view(), name="Concluir_pedido"),

    #path('pedido/editar/<id_produto>', PedidoUpdateView.as_view(), name='editar_pedido'),

    #path('produto/deletar/<id_produto>', PedidoDeleteView.as_view(), name='deletar_pedido'),

    path('tipo_entrega/', TipoEntregaListView.as_view(), name='tipo_entrega'),

    path('busca/<str:busca>', BuscaView.as_view(), name='busca'),

    path('status/', EnviaEmailView.as_view(), name='Envia email'),

    #Relatorio de preço de pedidos
    path('relatorio/pedidos', RelatorioTotalPagoPedidoView.as_view(), name='relatorio_pedido_list'),
    
    path('pedidosabertos/<int:id_restaurante>', PedidosAbertosRestaurante.as_view(), name='Pedido_aberto'),

    path('relatorio/tipo_pagamento', RelatorioTipoPagamento.as_view(), name='relatorio_tipo_pagamento'),
    #cartao por id de usuario
    path('cartao-usuario/<int:id_usuario>', CartaoUsuarioListView.as_view(), name='cartao_usuario'),

    #cartao especifico
    path('cartao/<int:id_cartao>', CartaoListView.as_view(), name='cartao_list'),

    #Criar Cartao
    path('cartao/criar', CartaoCreateView.as_view(), name='cartao_create'),

    #Deletar Cartao
    path('deletar/cartao/<int:id_cartao>', CartaoDeleteView.as_view(), name='cartao_delete'),

    #Atualizar Cartao
    path('atualizar/cartao/<int:id_cartao>', CartaoUpdateView.as_view(), name='cartao_update'),
]


