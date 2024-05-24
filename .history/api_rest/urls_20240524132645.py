from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreateAPIView.as_view(), name='user-list-create'),
    path('declarantes/', views.DeclaranteListCreateAPIView.as_view(), name='declarante-list'),
    path('declarantes/<str:cpf>/', views.DeclaranteDetailAPIView.as_view(), name='declarante-detail'),
    path('declaracoes/', views.DeclaracoesListCreateAPIView.as_view(), name='declarante-list'),
    path('declaracoes/create', views.DeclaracoesCreateAPIView.as_view(), name='declarante-list-create'),
]