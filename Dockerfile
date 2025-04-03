# Use a imagem base do Python
FROM python:3.13-slim

# Defina o diretório de trabalho
WORKDIR /app

# Defina argumentos de construção para as variáveis de ambiente
ARG USUARIO
ARG SENHA
ARG HOST
ARG PORTA_MYSQL
ARG BANCO_DE_DADOS

# Defina variáveis de ambiente usando os argumentos de construção
ENV USUARIO=$USUARIO
ENV SENHA=$SENHA
ENV HOST=$HOST
ENV PORTA_MYSQL=$PORTA_MYSQL
ENV BANCO_DE_DADOS=$BANCO_DE_DADOS

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt

# Instale as dependências (se houver)
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta em que o aplicativo será executado
EXPOSE 5000

# Copie os arquivos do aplicativo para o contêiner
COPY . .

# Comando para executar o aplicativo
CMD ["flask", "run", "--debug"]