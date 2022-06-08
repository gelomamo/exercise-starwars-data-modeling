import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'Usuarios'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(10), nullable=False)
    fecha_subscripcion = Column(String(10), nullable=False)

class Personajes(Base):
    __tablename__ = 'Personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    info = Column(String(250), nullable=False)

class Vehiculos(Base):
    __tablename__ = 'Vehiculos'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    info = Column(String(250), nullable=False)

class Planetas(Base):
    __tablename__ = 'Planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    info = Column(String(250), nullable=False)

class Vehiculos_Favoritos(Base):
    __tablename__ = 'Vehiculos_Favoritos'
    id = Column(Integer, primary_key=True)
    Vehiculo_id = Column(Integer, ForeignKey('Vehiculos.id'))
    Usuario_id = Column(Integer, ForeignKey('Usuarios.id'))

class Planetas_Favoritos(Base):
    __tablename__ = 'Planetas_Favoritos'
    id = Column(Integer, primary_key=True)
    Vehiculo_id = Column(Integer, ForeignKey('Planetas.id'))
    Usuario_id = Column(Integer, ForeignKey('Usuarios.id'))

class Personajes_Favoritos(Base):
    __tablename__ = 'Personajes_Favoritos'
    id = Column(Integer, primary_key=True)
    Vehiculo_id = Column(Integer, ForeignKey('Personajes.id'))
    Usuario_id = Column(Integer, ForeignKey('Usuarios.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')