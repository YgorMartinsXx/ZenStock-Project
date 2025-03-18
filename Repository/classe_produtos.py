from sqlalchemy import (
    Column,
    Integer,
    String,
    DECIMAL,
    
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Produtos(Base):
    __tablename__ = 'PRODUTOS'

    cod_produto = Column(Integer, primary_key=True)
    nome_produto = Column(String(30), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(DECIMAL(7, 2), nullable=False)
    categoria = Column(String(40), nullable=False)
    descricao = Column(String(50))

