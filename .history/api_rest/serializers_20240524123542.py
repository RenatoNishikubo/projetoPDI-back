from rest_framework import serializers
from .models import User, Declarante, Endereco, Propriedade, Dependente

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DeclaranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependente
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

class DeclaracoesSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(many=True, read_only=True)
    propriedade = PropriedadeSerializer(many=True, read_only=True)
    dependente = DependenteSerializer(many=True, read_only=True)

    class Meta:
        model = Declarante
        fields = ['cpf', 'nome', 'nascimento', 'telefone', 'email', 'profissao', 'contaBancaria', 'created_at', 'updated_at', 'endereco', 'propriedade', 'dependente']
