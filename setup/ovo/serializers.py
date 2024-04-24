from rest_framework import serializers
from .models import Usuario, Endereco, Restaurante, Produto, Comanda, TipoPagamento, Pedido, Tipo_entrega

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'first_name','last_name','cpf', 'email', 'celular']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id_endereco', 'nome_da_rua', 'numero', 'complemento', 'ponto_de_referencia', 'favorito', 'id_usuario']

class LoginEmailSeializer(serializers.Serializer): ###
    email = serializers.EmailField()

class LoginCelularSeializer(serializers.Serializer): ###
    celular = serializers.CharField()

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ['id_restaurante', 'nome_restaurante', 'sobre', 'endereco', 'cnpj', 'horario_funcionamento', 'id_tipo_entrega']

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id_produto', 'nome', 'descricao', 'preco', 'id_restaurante']

class ComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fields = ['id_comanda', 'id_produto', 'quantidade']

class TipoPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPagamento
        fields = ['id_tipo_pagamento', 'nome']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id_pedido', 'id_usuario', 'id_restaurante', 'id_tipo_entrega', 'valor_final', 'frete', 'id_tipo_pagamento', 'id_comanda']


class TipoEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_entrega
        fields = ['id_tipo_entrega', 'nome_tipo_entrega', 'tarifa']