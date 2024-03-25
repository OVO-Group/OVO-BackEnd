from django.db import models

# Create your models here.

#ALTERAR PARA ABSTRACT_USER
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome_completo = models.CharField(max_length = 45, null = False, blank = False, )
    cpf = models.CharField(max_length = 14, unique=True, null = False, blank = False)
    email = models.EmailField(unique=True, null = False, blank = False)
    celular = models.CharField(max_length=15, unique = True, null = False, blank = False)

    def __str__(self):
        return self.nome_completo

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

