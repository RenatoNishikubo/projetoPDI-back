from rest_framework import serializers
from .models import User, Declarante, Endereco, Propriedade, Dependente

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class PropriedadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propriedade
        fields = '__all__'

class DependenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependente
        fields = '__all__'

class DeclaranteSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    propriedade = PropriedadeSerializer(many=True)
    dependente = DependenteSerializer(many=True)

    class Meta:
        model = Declarante
        fields = ['cpf', 'nome', 'nascimento', 'telefone', 'email', 'profissao', 'contaBancaria', 'created_at', 'updated_at', 'endereco', 'propriedade', 'dependente']
