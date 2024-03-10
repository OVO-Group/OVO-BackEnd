from django.db import models

# Create your models here.


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