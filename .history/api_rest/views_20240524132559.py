from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Declarante
from .serializers import UserSerializer, DeclaracoesSerializer, DeclaranteSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeclaracoesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Declarante.objects.all()
    serializer_class = DeclaracoesSerializer

class DeclaracoesCreateAPIView(APIView):
    def post(self, request, format=None):
        serializer = DeclaracoesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeclaranteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Declarante.objects.all()
    serializer_class = DeclaranteSerializer

class DeclaranteDetailAPIView(APIView):
    def get(self, request, cpf, format=None):
        try:
            declarante = Declarante.objects.get(cpf=cpf)
        except Declarante.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = DeclaranteSerializer(declarante)
        return Response(serializer.data)