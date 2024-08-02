# example/urls.py
from django.urls import path
from .views import index, Fornecedores, CriarFornecedorAPIView, FornecedoresPorConsumo
from example.views import index


urlpatterns = [
    path('', index, name='index'),  # URL para a view index
    path('fornecedores/', Fornecedores.as_view(), name='fornecedores_list_create'),  # URL para a ListCreateAPIView
    path('fornecedores/criar/', CriarFornecedorAPIView.as_view(), name='fornecedor_create'),  # URL para a CreateAPIView
    path('fornecedores/consumo/<int:consumo>/', FornecedoresPorConsumo.as_view(), name='fornecedores_por_consumo'),  # URL para a view FornecedoresPorConsumo
]
