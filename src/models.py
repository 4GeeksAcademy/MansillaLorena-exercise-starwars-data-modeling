import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False,unique=True)
    firstname= Column(String(30))
    email= Column(String(40),nullable=False,unique=True)
    password=Column(String(12),nullable=False)
    favorites_planets= relationship('Favorites_planets',back_populates='planet')
    favorites_characters= relationship('Favorites_characters',back_populates='character')

class Favorites_planets(Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    planet_id = Column(Integer,ForeignKey('planet.id'))
    planet=Column(Integer,ForeignKey('planet.id'))
    
    user = relationship('User',back_populates='favorites_planets')
    planet = relationship('Planet',back_populates='favorites_planets')
      
class Favorites_characters(Base):
    __tablename__='favorites_characters'
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('user.id'))
    character_id=Column(Integer,ForeignKey('character.id'))
    character= Column(Integer,ForeignKey('character.id'))
    
    user = relationship('User',back_populates='favorites_characters')
    character= relationship('Character',back_populates='favorites_characters')

class Planet(Base):
    __tablename__='planet'
    id=Column(Integer,primary_key=True)
    favorites_planets= relationship('Favorites_planets',back_populates='planet')

    
class Character(Base):
    __tablename__='character'
    id=Column(Integer,primary_key=True)
    favorites_characters= relationship('Favorites_characters',back_populates='character')

    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
