from .models import Usuario, Endereco, Restaurante, Produto, Comanda, TipoPagamento, Pedido, Tipo_entrega, Cartao
from rest_framework import viewsets, status
from .serializers import UsuarioSerializer, EnderecoSerializer, LoginEmailSeializer, LoginCelularSeializer, RestauranteSerializer, ProdutoSerializer, ComandaSerializer, TipoPagamentoSerializer, PedidoSerializer, TipoEntregaSerializer, RelatorioPedidoSerializer, CartaoSerializer
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
from django.core import serializers
from django.core.mail import send_mail
from django.utils.html import strip_tags
import datetime
import random

#CRUD usuário
    

class UserListView(APIView):
    def get(self, request, id_usuario):
        user = get_object_or_404(Usuario, id_usuario = id_usuario)
        serializer = UsuarioSerializer(user)
        
        return Response(serializer.data)

class UserCreateView(APIView):
    def post(self, request):
        data = request.data
        user = Usuario.objects.filter(email=data['email']).first()
        if not user:
            serializer = UsuarioSerializer(data=request.data)
            serializer.is_valid(raise_exception="True")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)             
        else:
            serializer = UsuarioSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
class GetEnderecoView(APIView):
    def get(self, request, id_endereco):
        endereco = get_object_or_404(Endereco, id_endereco = id_endereco)
        serializer = EnderecoSerializer(endereco)
        return Response(serializer.data)

class EnderecoUsuarioListView(APIView):
    def get(self, request, id_usuario):
        endereco = Endereco.objects.filter(id_usuario=id_usuario)
        serializer = EnderecoSerializer(endereco, many=True)
        return Response(serializer.data)

class EnderecoRestauranteListView(APIView):
    def get(self, request, id_restaurante):
        restaurante = get_object_or_404(Endereco, id_restaurante = id_restaurante)
        serializer = EnderecoSerializer(restaurante)
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
        print(request.data)
        serializer = EnderecoSerializer(endereco, data=request.data)
        print(serializer)
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
                return Response({'user_data': {'id_usuario': user.id_usuario, 'email': user.email}})
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

class ProdutoListAll(APIView):
    def get(self, request):
        produto = Produto.objects.all()
        serializer = ProdutoSerializer(produto, many=True)
        return Response(serializer.data)
        

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
            data = {'email':email}
            serializer = UsuarioSerializer(data=data)
            serializer.is_valid(raise_exception="True")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)             
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
    
class ComandaCreateView(APIView):
    def post(self, request):
        dados = request.data 

       
        dados_comanda = {'produtos': dados}

        serializer = ComandaSerializer(data=dados_comanda)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
    

class ComandaListView(APIView):
    def get(self, request, id_comanda):
        comanda = get_object_or_404(Comanda, id_comanda=id_comanda)
        serializer = ComandaSerializer(comanda)
        
        return Response(serializer.data) 
    

class ComandaUpdateView(APIView):
    def put(self, request, id_comanda):
        comanda = get_object_or_404(Comanda, id_comanda=id_comanda)
        serializer = ComandaSerializer(comanda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class ComandaDeleteView(APIView):
    def delete(self, request, id_comanda):
        comanda = get_object_or_404(Comanda, id_comanda=id_comanda)
        comanda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class TipoPagamentoListView(APIView):
    def get(self, request):
        tipo_pagamento = TipoPagamento.objects.all()
        serializer = TipoPagamentoSerializer(tipo_pagamento, many=True)

        return Response(serializer.data)
    
class TipoPagamentoCreateVIew(APIView):
    def post(self, request):
        serializer = TipoPagamentoSerializer(data=request.data)
        serializer.is_valid(raise_exception="True")
        serializer.save()

        return Response(serializer.data)
    
class TipoPagamentoUpdateView(APIView):
    def put(self, request, id_tipo_pagamento):
        tipo_pagamento = get_object_or_404(TipoPagamento, id_tipo_pagamento=id_tipo_pagamento)
        serializer = TipoPagamentoSerializer(tipo_pagamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
class TipoPagamentoDeleteView(APIView):
    def delete(self, request, id_tipo_pagamento):
        tipo_pagamento = get_object_or_404(TipoPagamento, id_tipo_pagamento=id_tipo_pagamento)
        tipo_pagamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PedidoListView(APIView):
    def get(self, request, id_pedido):
        pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)
    
class PedidoCreateView(APIView):
    def post(self, request):
        serializer = PedidoSerializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception="True")
        serializer.save()

        id_pedido = serializer.data.get('id_pedido')

        dados = request.data

        id_usuario = dados.get('id_usuario')
        usuario = Usuario.objects.get(id_usuario=id_usuario)

        id_comanda = dados.get('id_comanda')
        print(id_comanda)
        comanda = Comanda.objects.get(id_comanda=id_comanda)

        id_restaurante = dados.get('id_restaurante')
        restaurante = Restaurante.objects.get(id_restaurante=id_restaurante)

        status = dados.get('status')

        valor_final = dados.get('valor_final')
        frete = dados.get('frete')

        id_tipo_entrega = dados.get('id_tipo_entrega')
        tipo_entrega = Tipo_entrega.objects.get(id_tipo_entrega=id_tipo_entrega)

        id_tipo_pagamento = dados.get('id_tipo_pagamento')
        tipo_pagamento = TipoPagamento.objects.get(id_tipo_pagamento=id_tipo_pagamento)

        def gerar_nota(recipient_email):
            pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
            endereco = get_object_or_404(Endereco, id_restaurante=pedido.id_restaurante)
            produtos = pedido.id_comanda.produtos
            subject = 'Nota fiscal eletrônica'
            html_message = f"""
            <html>
            <head>
                <title>Nota fiscal eletrônica</title>
            </head>
            <body>
                <h2>Detalhes</h2>
                <table border="1">
                    <tr>
                        <th>Campo</th>
                        <th>Informação</th>
                    </tr>
                    <tr>
                        <th>Emitente</th>
                        <th>{pedido.id_restaurante.nome_restaurante}</th>
                    </tr>
                    <tr>
                        <th>CNPJ Emitente</th>
                        <th>{pedido.id_restaurante.cnpj}</th>
                    </tr>
                    <tr>
                        <th>Endereco Emitente</th>
                        <th>{endereco.logradouro}, {endereco.numero}</th>
                    </tr>
                    <tr>
                        <th>Destinatário</th>
                        <th>{pedido.id_usuario.first_name}</th>
                    </tr>
                    <tr>
                        <th>CPF Destinatário</th>
                        <th>{pedido.id_usuario.cpf}</th>
                    </tr>
                    <tr>
                        <th>Data da Emissão</th>
                        <th>{pedido.id_restaurante.nome_restaurante}</th>
                    </tr>
                    <tr>
                        <th>Data de Emissão</th>
                        <th>{datetime.datetime.now()}</th>
                    </tr>
                    <tr>
                        <th>Número da NF</th>
                        <th>{random.randint(10000, 99999)}</th>
                    </tr>
                </table>
                <h2>Produtos</h2>
                <table border="1">
                    <tr>
                        <th>Nome</th>
                        <th>Preço Unitário</th>
                        <th>Quantidade</th>
                        <th>Valor Total do Produto</th>
                    </tr>
            """

         
            valor_total_compra = sum(float(produto['preco']) * int(produto['quantidade']) for produto in produtos)

           
            for produto in produtos:
                preco_unitario = float(produto['preco'])
                quantidade = int(produto['quantidade'])
                valor_total_produto = preco_unitario * quantidade
                
                html_message += f"""
                    <tr>
                        <td>{produto['nome']}</td>
                        <td>{preco_unitario:.2f}</td>
                        <td>{quantidade}</td>
                        <td>{valor_total_produto:.2f}</td>
                    </tr>
                """

        
            html_message += f"""
                    <tr>
                        <td colspan="3">Valor Total da Compra</td>
                        <td>{valor_total_compra:.2f}</td>
                    </tr>
                </table>
            </body>
            </html>
            """

            plain_message = strip_tags(html_message)
            from_email = "gabrielduartecarneiro@gmail.com"
            send_mail(subject, plain_message, from_email, [recipient_email], html_message=html_message)
        
        recipient_email = usuario.email

        gerar_nota(recipient_email)

        data = {
            'id_pedido' : id_pedido,
            'usuario': serializers.serialize('json', [usuario]),
            'comanda': serializers.serialize('json', [comanda]),
            'restaurante': serializers.serialize('json', [restaurante]),
            'status': status,
            'valor_final': valor_final,
            'frete': frete,
            'tipo_entrega': serializers.serialize('json', [tipo_entrega]),
            'tipo_pagamento': serializers.serialize('json', [tipo_pagamento]),
        }

        Pedido.objects.filter(id_comanda=None).delete()
                

        return Response(data)
    
class PedidoUpdateView(APIView):
    def put(self, request, id_pedido):
        pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
        novo_status = "concluido"
        pedido.status = novo_status
        pedido.save()
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)
    
class PedidoDeleteView(APIView):
    def delete(self, request, id_pedido):
        pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
        pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class TipoEntregaListView(APIView):
    def get(self, request):
        tipo_entrega = Tipo_entrega.objects.all()
        serializer = TipoEntregaSerializer(tipo_entrega, many=True)

        return Response(serializer.data)
    
class BuscaView(APIView):
    def get(self, request, busca):
        restaurantes = Restaurante.objects.filter(nome_restaurante__icontains=busca)
        produtos = Produto.objects.filter(nome__icontains=busca)
        
        serializer_restaurantes = RestauranteSerializer(restaurantes, many=True)
        serializer_produtos = ProdutoSerializer(produtos, many=True)

        data = {
            'restaurantes': serializer_restaurantes.data,
            'produtos': serializer_produtos.data
        }
        
        return Response(data)
    
class RelatorioTotalPagoPedidoView(APIView):
    def get(self, request):
        pedidos = Pedido.objects.all()
        serializer = RelatorioPedidoSerializer(pedidos, many=True)
        return Response(serializer.data)
    
class EnviaEmailView(APIView):
    def post(self,request):
        print(request.data)
        subject = 'Atualização do pedido'
        html_message = f"""
        <html>
        <head>
            <title>{request.data.get('title')}</title>
        </head>
        <body>
            <h2>{request.data.get('h2')}</h2>
            <p>{request.data.get('p')}</p>
        </body>
        </html>
        """
        recipient_email = request.data.get('email')

        plain_message = strip_tags(html_message)
        from_email = "gabrielduartecarneiro@gmail.com"
        send_mail(subject, plain_message, from_email, [recipient_email], html_message=html_message)

        data = {
            'Status' : 'Enviado'
        }
    
        return Response(data)
    
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pedido, Comanda
from .serializers import PedidoSerializer, ComandaSerializer

class PedidosAbertosRestaurante(APIView):
    def get(self, request, id_restaurante):
        pedidos = Pedido.objects.filter(status="Ativo", id_restaurante=id_restaurante)
        
        pedidos_completos = []
        
        for pedido in pedidos:
            pedido_serializer = PedidoSerializer(pedido)
            
            comanda = pedido.id_comanda
            comanda_serializer = ComandaSerializer(comanda)
            
            pedido_completo = {
                'id_pedido': pedido.id_pedido,
                'pedido': pedido_serializer.data,
                'produtos': comanda_serializer.data['produtos']  
            }
            
            pedidos_completos.append(pedido_completo)
        
        return Response(pedidos_completos)


    
#View para listar os cartoes do usuario
class CartaoUsuarioListView(APIView):
    def get(self, request, id_usuario):
        cartao = Cartao.objects.filter(id_usuario=id_usuario)
        serializer = CartaoSerializer(cartao, many=True)
        return Response(serializer.data)

#View para listar cartao
class CartaoListView(APIView):
    def get(self, request, id_cartao):
        cartao = get_object_or_404(Cartao, id_cartao=id_cartao)
        serializer = CartaoSerializer(cartao)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CartaoCreateView(APIView):
    def post(self, request):
        serializer = CartaoSerializer(data=request.data)
        serializer.is_valid(raise_exception='True')
        serializer.save()
        return Response(serializer.data)