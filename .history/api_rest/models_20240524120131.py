from django.db import models

class User(models.Model):
    user_nickname = models.CharField(primary_key=True, max_length=20, default='')
    user_name = models.CharField(max_length=150, default='')
    user_email = models.EmailField(default='')
    user_age = models.IntegerField(default=0)

class Declarante(models.Model):
    cpf = models.CharField(primary_key=True, max_length=20, default='')
    nome = models.CharField(max_length=150, default='')
    nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField(default='')
    profissao = models.CharField(max_length=100, default='')
    contaBancaria = models.CharField(max_length=30, default='')
    created_at = models.DateField()
    updated_at = models.DateField()

class Endereco(models.Model):
    declarante_id = models.ForeignKey(Declarante, related_name='endereco')
    cep = models.CharField(max_length=30, default='')
    rua = models.CharField(max_length=100, default='')
    numero = models.IntegerField(default=0)
    bairro = models.CharField(max_length=100, default='')
    cidade = models.CharField(max_length=100, default='')
    estado = models.CharField(max_length=100, default='')
    complemento = models.CharField(max_length=150, default='')

class Propriedade(models.Model):
    declarante_id = models.ForeignKey(Declarante, related_name='propriedade')
    tipo = models.CharField(max_length=20, default='')
    anoCompra = models.IntegerField(default=0)
    valorCompra = models.CharField(max_length=20, default='')
    anoVenda = models.IntegerField(default=0)
    valorVenda = models.CharField(max_length=20, default='')