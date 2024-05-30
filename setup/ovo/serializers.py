from rest_framework import serializers
from .models import Usuario, Endereco, Restaurante, Produto, Comanda, TipoPagamento, Pedido, Tipo_entrega, Cartao
from django.db.models.fields import DecimalField
from decimal import Decimal
from django.forms.models import model_to_dict

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'first_name','last_name','cpf', 'email', 'celular']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id_endereco', 'logradouro', 'bairro', 'cidade', 'uf', 'pais', 'numero', 'complemento', 'cep', 'ponto_de_referencia', 'tipo_endereco', 'id_usuario', 'id_restaurante']

class LoginEmailSeializer(serializers.Serializer):
    email = serializers.EmailField()

class LoginCelularSeializer(serializers.Serializer):
    celular = serializers.CharField()

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ['id_restaurante', 'nome_restaurante', 'sobre', 'cnpj', 'horario_funcionamento', 'id_tipo_entrega']

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id_produto', 'nome', 'descricao', 'preco', 'id_restaurante']

class ComandaSerializer(serializers.ModelSerializer):
    produtos = serializers.JSONField()

    class Meta:
        model = Comanda
        fields = ['id_comanda', 'produtos']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        produtos = representation.get('produtos')
        if produtos:
            for produto in produtos:
                for key, value in produto.items():
                    if isinstance(value, Decimal):
                        produto[key] = float(value)
        return representation

class TipoPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPagamento
        fields = ['id_tipo_pagamento', 'nome']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id_pedido', 'id_usuario', 'id_restaurante', 'id_tipo_entrega', 'valor_final', 'frete', 'id_tipo_pagamento', 'id_comanda', 'status', 'id_cartao', 'data']


class TipoEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_entrega
        fields = ['id_tipo_entrega', 'nome_tipo_entrega', 'tarifa']

class RelatorioPedidoSerializer(serializers.ModelSerializer):
    nome_restaurante = serializers.CharField(source='id_restaurante.nome_restaurante')
    id_tipo_entrega = serializers.CharField(source='id_tipo_entrega.nome_tipo_entrega')
    class Meta:
        model = Pedido
        fields = ['nome_restaurante', 'id_pedido', 'valor_final', 'id_tipo_entrega', 'frete']

class RelatorioTipoPagamentoSerializer(serializers.ModelSerializer):
    nome_restaurante = serializers.CharField(source='id_restaurante.nome_restaurante')
    tipo_pagamento = serializers.CharField(source='id_tipo_pagamento.nome')
    class Meta:
        model = Pedido
        fields = ['nome_restaurante','tipo_pagamento', 'valor_final', 'data', 'id_pedido']
class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = ['id_cartao', 'numero_cartao', 'data_validade', 'cvv', 'cpf_cnpj_titular', 'apelido_cartao', 'id_usuario']
