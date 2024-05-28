from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#ALTERAR PARA ABSTRACT_USER
class Usuario(AbstractUser):
    id_usuario = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45, null=True, blank=True)
    last_name = models.CharField(max_length=45, null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    celular = models.CharField(max_length=15, unique=True, null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    last_login = models.CharField(max_length=30, null=True, blank=True)
    is_superuser = models.CharField(max_length=1, null=True, blank=True)
    username = models.CharField(max_length=30, null=True, blank=True)
    is_staff = models.CharField(max_length=1, null=True, blank=True)
    is_active = models.CharField(max_length=1, null=True, blank=True)
    date_joined = models.CharField(max_length=20, null=True, blank=True)
    # Adicione campos adicionais se necessário

    def __str__(self):
        return self.first_name

    class Meta:
        # Define um nome amigável para o modelo de usuário personalizado
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    # Defina related_name personalizados para evitar conflitos com o modelo de usuário padrão
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='grupos',
        blank=True,
        related_name='custom_user_groups'  # Define um related_name personalizado
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='permissões do usuário',
        blank=True,
        related_name='custom_user_permissions'  # Define um related_name personalizado
    )

class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    nome_da_rua = models.CharField(max_length = 100, null = False, blank = False)
    numero = models.CharField(max_length = 7, null = False)
    complemento = models.CharField(max_length = 45, null = True, blank = True)
    ponto_de_referencia = models.CharField(max_length = 100, null = True, blank = True)
    favorito = models.BinaryField()
    id_usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

    def __str__(self):
        return self.nome_da_rua

class Tipo_entrega(models.Model):
    id_tipo_entrega = models.AutoField(primary_key=True)
    nome_tipo_entrega = models.CharField(max_length=45, null=False)
    tarifa = models.DecimalField(null = False, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome_tipo_entrega

class Restaurante(models.Model):
    id_restaurante = models.AutoField(primary_key=True)
    nome_restaurante = models.CharField(max_length = 50, null = False, blank = False)
    sobre = models.CharField(max_length = 200, null = True, blank = True)
    endereco = models.CharField(max_length = 100, null = False)
    cnpj = models.CharField(max_length = 14, null = False)
    horario_funcionamento = models.CharField(max_length = 150, null = False, blank = True)
    id_tipo_entrega = models.ForeignKey(Tipo_entrega, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.nome_restaurante


class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length = 45, null = False)
    descricao = models.CharField(max_length = 50, null = False)
    preco = models.DecimalField(null = False, max_digits=10, decimal_places=2)
    id_restaurante = models.ForeignKey(Restaurante, on_delete = models.CASCADE)

    def __str__(self):
        return self.nome


class TipoPagamento(models.Model):
    id_tipo_pagamento = models.AutoField(primary_key=True)
    nome= models.CharField(max_length=45, null=False, blank=False)

    def __str__(self):
        return self.nome

class Comanda(models.Model):
    id_comanda = models.AutoField(primary_key=True)
    produtos = models.JSONField(null=False, blank=False, default=dict)

    
class Cartao(models.Model):
    id_cartao = models.AutoField(primary_key=True)
    numero_cartao = models.CharField(max_length=16, blank=False, null=False)
    nome_titular = models.CharField(max_length=45, blank=False, null=False)
    data_validade = models.DateField(null=False, blank=False)
    cvv = models.CharField(max_length=3, blank=False, null=False)
    apelido_cartao = models.CharField(max_length=45, null=False, blank=False)
    cpf_cnpj_titular = models.CharField(max_length=14, null=False, blank=False)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    id_restaurante = models.ForeignKey(Restaurante, on_delete = models.CASCADE)
    id_tipo_entrega = models.ForeignKey(Tipo_entrega, on_delete = models.CASCADE)
    valor_final = models.DecimalField(null = False, max_digits=10, decimal_places=2)
    frete = models.DecimalField(null = False, max_digits=10, decimal_places=2)
    id_tipo_pagamento= models.ForeignKey(TipoPagamento, on_delete = models.CASCADE)
    id_comanda = models.ForeignKey(Comanda, null = True ,on_delete = models.CASCADE)
    status = models.CharField(max_length=30, null=False, blank=False, default='Inativo')
    id_cartao = models.ForeignKey(Cartao, blank=True, null=True, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.valor_final


