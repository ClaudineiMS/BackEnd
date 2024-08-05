import graphene
import json

# Função para ler dados do arquivo JSON
def load_data():
    with open('fornecedores.json', 'r') as file:
        return json.load(file)

# Define o tipo GraphQL para o fornecedor
class FornecedorType(graphene.ObjectType):
    nome = graphene.String()
    limite_minimo = graphene.Float()
    numero_total_de_clientes = graphene.Int()
    custo = graphene.Float()
    avaliacao_media_dos_clientes = graphene.String()
    logo = graphene.String()
    estado_de_origem = graphene.String()

# Define a Query para retornar fornecedores com base no consumo
class Query(graphene.ObjectType):
    fornecedores = graphene.List(
        FornecedorType,
        consumo=graphene.Float() 
    )

    def resolve_fornecedores(self, info, consumo=None):
        fornecedores = load_data()
        if consumo is not None:
            # Filtra fornecedores com base no consumo
            fornecedores = [fornecedorees for fornecedorees in fornecedores if fornecedorees['limite_minimo'] <= consumo]
        return fornecedores

#Esquema GraphQL
schema = graphene.Schema(query=Query)
