from sqlalchemy import (
    Column,
    Integer,
    DateTime,
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Pedidos(Base):
    __tablename__ = 'PEDIDOS'

    id_pedido = Column(Integer, primary_key=True, autoincrement=True)
    data_pedido = Column(DateTime, nullable=False, default='CURRENT_TIMESTAMP')