from sqlalchemy import (
    Column,
    Integer,
    String,
    DECIMAL,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'PRODUTOS'

    cod_produto = Column(Integer, primary_key=True)
    nome_produto = Column(String(30), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(DECIMAL(7, 2), nullable=False)
    categoria = Column(String(40), nullable=False)
    descricao = Column(String(50))

    def __repr__(self):
        return f"<Produto {self.nome_produto}>"

    def to_dict(self):
        """Converte o objeto Produto para um dicionário."""
        return {
            'cod_produto': self.cod_produto,
            'nome_produto': self.nome_produto,
            'quantidade': self.quantidade,
            'preco_unitario': str(self.preco_unitario),  # Convertendo para string para evitar problemas com JSON
            'categoria': self.categoria,
            'descricao': self.descricao
        }
