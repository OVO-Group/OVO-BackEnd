from rest_framework import serializers
from .models import Usuario, Endereco, Restaurante, Produto

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

