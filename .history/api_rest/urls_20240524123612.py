from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreateAPIView.as_view(), name='user-list-create'),
    path('declarantes/', views.DeclaranteListCreateAPIView.as_view(), name='declarante-list-create'),
    path('declaracoes/', views.DeclaracoesListCreateAPIView.as_view(), name='declarante-list-create'),
]