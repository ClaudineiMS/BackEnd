#imagem oficial do Python
FROM python:3.9-slim

#diretório de trabalho dentro do contêiner
WORKDIR /app

#Dependências da aplicação
COPY requirements.txt .

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copia o restante do código do aplicativo para o contêiner
COPY . .

# Expõe a porta em que o servidor Django será executado
EXPOSE 8000

# Inicia o servidor Django
CMD ["gunicorn --bind 0.0.0.0:8000 --timeout 120 api.wsgi:application"]

