from rest_framework import serializers
from .models import User, Declarante, Endereco, Propriedade, Dependente

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    declarante_id = serializers.PrimaryKeyRelatedField(source='declarante', read_only=True)
    class Meta:
        model = Endereco
        fields =  ['declarante_id', 'cep', 'rua', 'numero', 'bairro', 'cidade', 'estado', 'complemento']

class PropriedadeSerializer(serializers.ModelSerializer):
    declarante_id = serializers.PrimaryKeyRelatedField(source='declarante', read_only=True)
    class Meta:
        model = Propriedade
        fields = '__all__'

class DependenteSerializer(serializers.ModelSerializer):
    declarante_id = serializers.PrimaryKeyRelatedField(source='declarante', read_only=True)
    class Meta:
        model = Dependente
        fields = '__all__'

class DeclaranteSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(read_only=True)
    propriedade = PropriedadeSerializer(many=True, read_only=True)
    dependente = DependenteSerializer(many=True, read_only=True)

    class Meta:
        model = Declarante
        fields = ['cpf', 'nome', 'nascimento', 'telefone', 'email', 'profissao', 'contaBancaria', 'created_at', 'updated_at', 'endereco', 'propriedade', 'dependente']
