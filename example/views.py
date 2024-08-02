# example/views.py
from datetime import datetime
from django.http import HttpResponse
from rest_framework import generics
from .models import Fornecedor
from .serializers import FornecedorSerializer
from django.http import JsonResponse
from django.views import View

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Teste ---- 2!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)


class Fornecedores(generics.ListCreateAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class CriarFornecedorAPIView(generics.CreateAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class FornecedoresPorConsumo(View):
    def get(self, request, *args, **kwargs):
        consumo = self.kwargs['consumo']
        fornecedores = Fornecedor.objects.filter(limite_mínimo__lte=consumo)

        # Cria uma lista de dicionários com os dados dos fornecedores
        fornecedores_data = list(fornecedores.values('nome', 'estado_de_origem', 'custo', 'limite_mínimo', 'numero_total_de_clientes', 'avaliação_média_dos_clientes','logo'))

        # Retorna os dados em formato JSON
        return JsonResponse(fornecedores_data, safe=False)