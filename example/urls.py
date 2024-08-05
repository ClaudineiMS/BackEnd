from django.urls import path
from example.views import index, fornecedores_view, FornecedoresPorConsumo
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from example.schema import schema 

urlpatterns = [
    path('', index, name='index'),  # URL para a view index
    path('fornecedores/', fornecedores_view, name='fornecedores'),
    path('fornecedores/consumo/<int:consumo>/', FornecedoresPorConsumo.as_view(), name='fornecedores_por_consumo'),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]