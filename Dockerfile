# Use a imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos do aplicativo para o contêiner
COPY . /app

# Instale as dependências (se houver)
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta em que o aplicativo será executado
EXPOSE 5000

# Comando para executar o aplicativo
CMD ["python", "app.py"]