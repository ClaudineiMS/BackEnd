## Branches

A branch **main** está configurada para funcionar no **Vercel**.

A branch **teste_automatizado_back** está configurada com os testes automatizados e para funcionar dockerizada.

backend no **Vercel:** https://django-backend-amber.vercel.app/

Endpoints: 

https://django-backend-amber.vercel.app/fornecedores

https://django-backend-amber.vercel.app/fornecedores/consumo/800

## Configuração do ambiente virtual

Para criar e configurar um ambiente virtual para a aplicação siga os passos abaixo:

**Crie um ambiente virtual com Python 3.9**

Execute o seguinte comando para criar um ambiente virtual chamado **venv**:

```bash
python3.9 -m venv venv
```
No Linux: 

```bash
source venv/bin/activate
```

Com a venv ativa va até o diretório django-hello-world e execute:
```bash
pip install -r requirements.txt
```

## Executando o ambiente 
Execute:
```bash
python3.9 manage.py runserver
```


## Django testes automatizados

Navegue até o diretório django-hello-world e execute
```bash
python3.9 manage.py test --settings=api.test_settings
```

## Tipos de teste

Seram feitos 5 testes simples 

**test_index_url**: Verifica se a URL para a view index está funcionando corretamente e retorna o código de status HTTP 200 OK.

**test_fornecedores_url**: Verifica se a URL para a view fornecedores está funcionando corretamente e retorna o código de status HTTP 200 OK.

**test_fornecedores_por_consumo_url**: Verifica se a URL para a view fornecedores_por_consumo com um parâmetro de consumo válido retorna o código de status HTTP 200 OK.

**test_fornecedores_por_consumo_nao_atendido**: Verifica se a URL para a view fornecedores_por_consumo com um parâmetro de consumo que não atende a nenhum fornecedor ainda retorna o código de status HTTP 200 OK.

**test_fornecedores_por_consumo_vazio**: Verifica se a URL para a view fornecedores_por_consumo com um parâmetro de consumo vazio (None) retorna o código de status HTTP 200 OK.


## Como dockerizar a aplicação

```bash
docker-compose build
docker-compose up
```

A aplicação está disponivel na porta 8000