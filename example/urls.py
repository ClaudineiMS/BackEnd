from django.urls import path
from example.views import index, fornecedores_view, FornecedoresPorConsumo

urlpatterns = [
    path('', index, name='index'),  # URL para a view index
    path('fornecedores/', fornecedores_view, name='fornecedores'),
    path('fornecedores/consumo/<int:consumo>/', FornecedoresPorConsumo.as_view(), name='fornecedores_por_consumo'),
]