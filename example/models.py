
"""
Este módulo define o modelo Fornecedor, que representa informações sobre os fornecedores de uma empresa.

Campos:
- nome: Nome do fornecedor (máximo de 100 caracteres).
- estado_de_origem: Estado de origem do fornecedor (máximo de 15 caracteres).
- custo: Custo associado ao fornecedor (valor decimal com até 10 dígitos e 2 casas decimais).
- limite_mínimo: Limite mínimo de pedido para o fornecedor (inteiro).
- numero_total_de_clientes: Número total de clientes atendidos pelo fornecedor (inteiro).
- avaliação_média_dos_clientes: Avaliação média dos clientes para o fornecedor (valor decimal com até 10 dígitos e 2 casas decimais).
- logo: Caminho para o logo do fornecedor (imagem, opcional).
"""
from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.ImageField(blank=True, null=True)
    estado_de_origem = models.CharField(max_length=15)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    limite_mínimo = models.PositiveIntegerField()  # Somente valores positivos
    numero_total_de_clientes = models.PositiveIntegerField()  # Somente valores positivos
    avaliação_média_dos_clientes = models.DecimalField(max_digits=10, decimal_places=2)
   
    def __str__(self):
        return f"{self.nome} - {self.estado_de_origem}"
