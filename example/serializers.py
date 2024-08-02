"""
Classes:
    Serializer para o modelo Fornecedor, incluindo todos os campos do modelo e garante que dados invalidos não sejam inseridos ( valores negativos )
"""
from rest_framework import serializers
from .models import Fornecedor

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'
    
    def validate(self, data):
        limite_minimo = data.get('limite_mínimo')
        numero_total_de_clientes = data.get('numero_total_de_clientes')
        
        if limite_minimo is not None and limite_minimo < 0:
            raise serializers.ValidationError("O limite mínimo de kWh não pode ser negativo.")
        
        if numero_total_de_clientes is not None and numero_total_de_clientes < 0:
            raise serializers.ValidationError("O número total de clientes não pode ser negativo.")
        
        return data

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'
