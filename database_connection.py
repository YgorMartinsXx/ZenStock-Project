# imports
import os
from dotenv import load_dotenv


# gera os parâmetros para Acessar o banco de dados
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
host = os.getenv("HOST")
banco_de_dados = os.getenv("BANCO_DE_DADOS")

target = f"mysql+pymysql://{usuario}:{senha}@{host}/{banco_de_dados}"
