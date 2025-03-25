from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    DECIMAL,
    CheckConstraint
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Fornecedores(Base):
    __tablename__ = 'FORNECEDORES'

    cnpj = Column(String(14), primary_key=True)
    nome_fornecedor = Column(String(40), nullable=False)
    endereco = Column(String(40), nullable=False)
    email = Column(String(40), nullable=False)
    telefone = Column(String(11), nullable=False)
