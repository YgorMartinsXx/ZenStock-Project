from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Fornece(Base):
    __tablename__ = 'FORNECE'

    id_pedido = Column(Integer, ForeignKey('PEDIDOS.id_pedido', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    cnpj_fornecedor = Column(String(14), ForeignKey('FORNECEDORES.cnpj', ondelete='CASCADE', onupdate='CASCADE'),)
    cod_produto = Column(Integer, ForeignKey('PRODUTOS.cod_produto', ondelete='CASCADE', onupdate='CASCADE'),)
    quantidade = Column(Integer)
