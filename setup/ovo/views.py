from .models import Usuario, Endereco, Restaurante, Produto
from rest_framework import viewsets, status
from .serializers import UsuarioSerializer, EnderecoSerializer, LoginEmailSeializer, LoginCelularSeializer, RestauranteSerializer, ProdutoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.db.models import Q
import requests
from random import randint
from django.http import HttpResponse
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
#CRUD usuário
    

class UserListView(APIView):
    def get(self, request, id_usuario):
        user = get_object_or_404(Usuario, id_usuario=id_usuario)
        serializer = UsuarioSerializer(user)
        
        return Response(serializer.data)

class UserCreateView(APIView):
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception="True")
        serializer.save()
        return Response(serializer.data)

class UserUpdateView(APIView):
    def put(self, request, id_usuario):
        
        user = get_object_or_404(Usuario, id_usuario=id_usuario)
        serializer = UsuarioSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDeleteView(APIView):
    def delete(self, request, id_usuario):
        user = get_object_or_404(Usuario, id_usuario=id_usuario)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

#CRUD Endereco


class EnderecoListView(APIView):
    def get(self, request, id_endereco):
        endereco = get_object_or_404(Endereco, id_endereco=id_endereco)
        serializer = EnderecoSerializer(endereco)
        
        return Response(serializer.data)
    
class EnderecoCreateView(APIView):
    def post(self, request):
        serializer = EnderecoSerializer(data=request.data)
        serializer.is_valid(raise_exception="True")
        serializer.save()
        return Response(serializer.data)
    
class EnderecoUpdateView(APIView):
    def put(self, request, id_endereco):
        endereco = get_object_or_404(Endereco, id_endereco=id_endereco)
        serializer = EnderecoSerializer(endereco, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EnderecoDeleteView(APIView):
    def delete(self, request, id_endereco):
        endereco = get_object_or_404(Endereco, id_endereco=id_endereco)
        endereco.delete()
        return Response("Usúario deletado com sucesso")            
    
#Rotas de Login

#Gera código de verificação e envia email
def gerar_e_enviar_codigo(email):
    numeros = [str(randint(0, 9)) for _ in range(6)]
    codigo = ''.join(numeros)
    send_mail('Código de Verificação DJANGO', f'Código de verificação é {codigo}', 'gabrielduartecarneiro@gmail.com', [email])
    return codigo

class LoginEmailView(APIView):
    def post(self, request):
        serializer = LoginEmailSeializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data['email']
        '''
        user = Usuario.objects.filter(email=email).first()
        if not user:
            return Response({'message': 'E-mail não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        '''
        emailUsuario = request.data["email"]
        codigo = gerar_e_enviar_codigo(emailUsuario)

        request.session['codigo_verificacao'] = codigo
        request.session['email_usuario'] = email

        return Response({"mensagem":"Email Enviado!", "codigo_verificacao": codigo})
    
class VerificaCodigo(APIView):
    def post(self, request):
        #codigoGerado = request.session.get('codigo_verificacao')
        codigo_usuario = request.data["codigo"]
        cod_enviado = request.data["cod_enviado"]
        email = request.data["email"]
        print(request)

        if codigo_usuario == cod_enviado:
            user = Usuario.objects.filter(email=email).first()
            if user:
                refresh = RefreshToken.for_user(user)
                token = str(refresh.access_token)
                return Response({'user_data': {'id': user.id_usuario, 'email': user.email, 'token': token}})
            else:
                return Response('usuário não cadastrado')
        return Response('Código de verificação inválido')

class LoginCelularView(APIView):
    def post(self, request):
        serializer = LoginCelularSeializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        celular = serializer.validated_data['celular']
        user = Usuario.objects.filter(celular=celular).first()
        if not user:
            return Response({'message': 'Celular não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UsuarioSerializer(user)
        return Response(serializer.data)
        
        #Autenticação com Twilio


class EnderecoUsuarioListView(APIView):
    def get(self, request, id_usuario):
        enderecos = Endereco.objects.filter(id_usuario=id_usuario)
        serializer = EnderecoSerializer(enderecos, many=True)
        print(serializer)
        
        return Response(serializer.data)

class RestauranteListView(APIView):
    def get(self, request):
        restaurante = Restaurante.objects.all()
        serializer = RestauranteSerializer(restaurante, many=True)
        return Response(serializer.data)
    
class RestauranteCreateView(APIView):
    def post(self, request):
        serializer = RestauranteSerializer(data=request.data)
        serializer.is_valid(raise_exception="True")
        serializer.save()
        return Response(serializer.data)
    
class RestauranteDeleteView(APIView):
    def delete(self, request, id_restaurante):
        restaurante = get_object_or_404(Restaurante, id_restaurante=id_restaurante)
        restaurante.delete()
        return Response("Restaurante deletado com sucesso")
    
class GetRestauranteView(APIView):
    def get(self, request, id_restaurante):
        restaurante = get_object_or_404(Restaurante, id_restaurante=id_restaurante)
        serializer = RestauranteSerializer(restaurante)
        return Response(serializer.data)
    
class RestauranteEditView(APIView):
    def put(self, request, id_restaurante):
        restaurante = Restaurante.objects.get(pk=id_restaurante)
        serializer = RestauranteSerializer(restaurante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetProdutoView(APIView):
    def get(self, request, id_produto):
        produto = get_object_or_404(Produto, id_produto=id_produto)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

class ProdutoListView(APIView):
    def get(self, request, id_restaurante):
        produto = Produto.objects.filter(id_restaurante=id_restaurante)
        serializer = ProdutoSerializer(produto, many=True)
        return Response(serializer.data)


class VerificaEmail(APIView):
    def post(self, request):
        email = request.body.decode('utf-8')
        user = Usuario.objects.filter(email=email).first()
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_200_OK)
        #email = request.data.get("email")
        #user = Usuario.objects.filter(email=email).first()
        
class ProdutoCreateView(APIView):
    def post(self, request):
        serializer = ProdutoSerializer(data=request.data)
        serializer.is_valid(raise_exception="True")
        serializer.save()
        return Response(serializer.data)
    
class ProdutoDeleteView(APIView):
    def delete(self, request, id_produto):
        produto = get_object_or_404(Produto, id_produto=id_produto)
        produto.delete()
        return Response("produto deletado com sucesso")
    
class ProdutoEditView(APIView):
    def put(self, request, id_produto):
        print(request.data)
        produto = Produto.objects.get(id_produto=id_produto)
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
