from rest_framework import serializers
from .models import Usuario, Endereco

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'nome_completo', 'cpf', 'email', 'celular']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id_endereco', 'nome_da_rua', 'numero', 'complemento', 'ponto_de_referencia', 'favorito', 'id_usuario']

class LoginEmailSeializer(serializers.Serializer):
    email = serializers.EmailField()

class LoginCelularSeializer(serializers.Serializer):
    celular = serializers.CharField()