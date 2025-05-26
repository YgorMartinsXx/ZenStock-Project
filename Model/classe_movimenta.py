from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Movimenta(Base):
    __tablename__ = 'MOVIMENTA'

    id_movimentacao = Column(Integer, primary_key=True, autoincrement=True)
    evento = Column(String(7), nullable=False)
    quantidade = Column(Integer, nullable=False)
    data_movimentacao = Column(DateTime, nullable=False, default='CURRENT_TIMESTAMP')
    cod_produto = Column(Integer, ForeignKey('PRODUTOS.cod_produto', ondelete='CASCADE', onupdate='CASCADE'))
    usuario = Column(String(17), ForeignKey('USUARIOS.login', ondelete='CASCADE', onupdate='CASCADE'))