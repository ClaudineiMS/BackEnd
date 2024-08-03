from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
import os
from django.conf import settings
import json

def index(request):
    html = f'''
    <html>
        <head>
            <style>
                body {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: 'Arial', sans-serif;
                    background-color: #f0f0f0;
                }}
                h1 {{
                    font-size: 2.5rem;
                    color: #333;
                }}
                p {{
                    font-size: 1.2rem;
                    color: #666;
                }}
            </style>
        </head>
        <body>
            <div>
                <h1>Desafio técnico!</h1>
            </div>
        </body>
    </html>
    '''
    return HttpResponse(html)


def fornecedores_view(request):
    # Caminho absoluto para o arquivo JSON
    json_path = os.path.join(settings.BASE_DIR, 'fornecedores.json')
    
    # Ler o conteúdo do arquivo JSON
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Retornar os dados JSON
    return JsonResponse(data, safe=False)

class FornecedoresPorConsumo(View):
    def get(self, request, consumo):
        # Caminho completo para o arquivo JSON
        json_path = os.path.join(settings.BASE_DIR, 'fornecedores.json')

        try:
            with open(json_path, 'r') as file:
                fornecedores = json.load(file)

            # Filtra fornecedores com consumo maior ou igual ao limite mínimo
            fornecedores_filtrados = [
                fornecedor for fornecedor in fornecedores
                if fornecedor.get('limite_mínimo', 0) <= consumo
            ]

            return JsonResponse(fornecedores_filtrados, safe=False)

        except FileNotFoundError:
            return JsonResponse({'error': 'Arquivo JSON não encontrado'}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Erro ao decodificar JSON'}, status=500)