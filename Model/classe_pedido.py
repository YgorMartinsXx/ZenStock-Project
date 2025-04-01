from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Pedidos(Base):
    __tablename__ = "PEDIDOS"

    id_Pedido = Column(Integer, primary_key=True, autoincrement=True)
    data_Pedido = Column(DateTime, nullable=False, default=func.current_timestamp())