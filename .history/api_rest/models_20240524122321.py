from django.db import models
from datetime import datetime

class User(models.Model):
    user_nickname = models.CharField(primary_key=True, max_length=20, default='')
    user_name = models.CharField(max_length=150, default='')
    user_email = models.EmailField(default='')
    user_age = models.IntegerField(default=0)
    user_password = models.CharField(max_length=20, default='')

class Declarante(models.Model):
    cpf = models.CharField(primary_key=True, max_length=20, default='')
    nome = models.CharField(max_length=150, default='')
    nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField(default='')
    profissao = models.CharField(max_length=100, default='')
    contaBancaria = models.CharField(max_length=30, default='')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        return super(Declarante, self).save(*args, **kwargs)

class Endereco(models.Model):
    declarante = models.ForeignKey(Declarante, related_name='endereco', on_delete=models.CASCADE)
    cep = models.CharField(max_length=30, default='')
    rua = models.CharField(max_length=100, default='')
    numero = models.IntegerField(default=0)
    bairro = models.CharField(max_length=100, default='')
    cidade = models.CharField(max_length=100, default='')
    estado = models.CharField(max_length=100, default='')
    complemento = models.CharField(max_length=150, default='')

class Propriedade(models.Model):
    declarante = models.ForeignKey(Declarante, related_name='propriedade', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, default='')
    anoCompra = models.IntegerField(default=0)
    valorCompra = models.CharField(max_length=20, default='')
    anoVenda = models.IntegerField(default=0)
    valorVenda = models.CharField(max_length=20, default='')

class Dependente(models.Model):
    declarante = models.ForeignKey(Declarante, related_name='dependente', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, default='')
    nome = models.CharField(max_length=150, default='')
    documento = models.CharField(max_length=20, default='')
    nascimento = models.DateField()