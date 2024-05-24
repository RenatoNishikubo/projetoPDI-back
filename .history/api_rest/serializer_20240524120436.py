from rest_framework import serializers
from .models import User, Declarante, Endereco, Propriedade, Dependente

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_nickname', 'user_name', 'user_email', 'user_age']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['cep', 'rua', 'numero', 'bairro', 'cidade', 'estado', 'complemento']

class PropriedadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propriedade
        fields = ['tipo', 'anoCompra', 'valorCompra', 'anoVenda', 'valorVenda']

class DependenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependente
        fields = ['tipo', 'nome', 'documento', 'nascimento']

class DeclaranteSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    propriedade = PropriedadeSerializer(many=True)
    dependente = DependenteSerializer(many=True)

    class Meta:
        model = Declarante
        fields = ['cpf', 'nome', 'nascimento', 'telefone', 'email', 'profissao', 'contaBancaria', 'created_at', 'updated_at', 'endereco', 'propriedade', 'dependente']
