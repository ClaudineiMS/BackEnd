from django.test import TestCase, Client
from django.urls import reverse

class URLTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_url(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)  # Verifica se o status é 200 OK

    def test_fornecedores_url(self):
        response = self.client.get(reverse('fornecedores'))
        self.assertEqual(response.status_code, 200)  

    def test_fornecedores_por_consumo_url(self):
        response = self.client.get(reverse('fornecedores_por_consumo', args=[500]))
        self.assertEqual(response.status_code, 200) 

    def test_fornecedores_por_consumo_nao_atentido(self):
        response = self.client.get(reverse('fornecedores_por_consumo', args=[100]))
        self.assertEqual(response.status_code, 200) 

    #Teste que falha
    def test_fornecedores_por_consumo_vazio(self):
        response = self.client.get(reverse('fornecedores_por_consumo', args=[None]))
        self.assertEqual(response.status_code, 200)  