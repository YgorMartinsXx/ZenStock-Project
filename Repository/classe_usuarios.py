

from sqlalchemy import (
    Column,
    String,
    CheckConstraint
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'USUARIOS'

    login = Column(String(17), primary_key=True)
    senha = Column(String(20), nullable=False)
    cargo = Column(String(15), nullable=False)

    __table_args__ = (
        CheckConstraint(cargo.in_(['Estoquista', 'Administrador']), name='check_cargo'),
    )