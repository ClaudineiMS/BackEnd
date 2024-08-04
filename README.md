## Branchs
A branch **main** está configurada para funcionar no vercel.

A branch **teste_automatizado_back** está configurada com os testes automatizados e para funcionar dockerizada ( ler tótpico: Como dockerizar a aplicação)


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

**test_fornecedores_por_consumo_nao_atentido**: Verifica se a URL para a view fornecedores_por_consumo com um parâmetro de consumo que não atende a nenhum fornecedor ainda retorna o código de status HTTP 200 OK.

**test_fornecedores_por_consumo_vazio**: Verifica se a URL para a view fornecedores_por_consumo com um parâmetro de consumo vazio (None) retorna o código de status HTTP 200 OK.


## Como dockerizar a aplicação

No arqruivo **wsgi.py** descomente a variávelo **application = get_wsgi_application()**

e comente a variável **app = get_wsgi_application()**

Após essa mudança execute: 

Para construir a imagem do Docker, execute o seguinte comando:

```bash
docker-compose build
docker-compose up
```

A aplicação está disponivel na porta 8000