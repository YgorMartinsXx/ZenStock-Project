from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# gera os parâmetros para Acessar o banco de dados
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
host = os.getenv("HOST")
banco_de_dados = os.getenv("BANCO_DE_DADOS")
porta = os.getenv("PORTA_MYSQL")

DATABASE_URL = f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco_de_dados}"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

if __name__ == '__main__':
    try:
        # teste conexao
        with engine.connect() as connection:
            print("Conexao bem-sucedida!")
    except Exception as e:
        print(f"Erro na conexao: {e}")
