from rest_framework import generics
from .models import User, Declarante
from .serializers import UserSerializer, DeclaranteSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeclaranteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Declarante.objects.all()
    serializer_class = DeclaranteSerializer