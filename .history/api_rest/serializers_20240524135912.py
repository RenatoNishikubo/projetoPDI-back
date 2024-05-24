from rest_framework import serializers
from .models import User, Declarante, Endereco, Propriedade, Dependente

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DeclaranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Declarante
        fields = ['cpf', 'nome', 'nascimento', 'telefone', 'email', 'profissao', 'contaBancaria']

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

class DeclaracoesSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(many=True)
    propriedade = PropriedadeSerializer(many=True)
    dependente = DependenteSerializer(many=True)

    class Meta:
        model = Declarante
        fields = ['cpf', 'nome', 'nascimento', 'telefone', 'email', 'profissao', 'contaBancaria', 'created_at', 'updated_at', 'endereco', 'propriedade', 'dependente']

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        propriedade_data = validated_data.pop('propriedade')
        dependente_data = validated_data.pop('dependente')

        declarante = Declarante.objects.create(**validated_data)

        for endereco in endereco_data:
            Endereco.objects.create(declarante=declarante, **endereco)

        for propriedade in propriedade_data:
            Propriedade.objects.create(declarante=declarante, **propriedade)

        for dependente in dependente_data:
            Dependente.objects.create(declarante=declarante, **dependente)

        return declarante