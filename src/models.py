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
    favorites_planets= relationship('Favorites_planets',back_populates='planetId_relationship')
    favorites_characters= relationship('Favorites_characters',back_populates='characterId_relationship')

class Favorites_planets(Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(50))
    planet_id = Column(Integer,ForeignKey('user.id'),unique=True)
    planetId_relationship= relationship('User',back_populates='favorites_planets')
    planet=Column(Integer,ForeignKey('planet.id'),unique=True)
    planet_relationship= relationship('Planet',back_populates='favorites_planets')
      
class Favorites_characters(Base):
    __tablename__='favorites_characters'
    id=Column(Integer,primary_key=True)
    user_id=Column(String(50))
    character_id=Column(Integer,ForeignKey('user.id'),unique=True)
    characterId_relationship= relationship('User',back_populates='favorites_characters')
    character= Column(Integer,ForeignKey('character.id'),unique=True)
    character_relationship= relationship('Character',back_populates='favorites_characters')

class Planet(Base):
    __tablename__=('planet')
    id=Column(Integer,primary_key=True)
    planet_id=Column(String(50))
    favorites_planets= relationship('Favorites_planets',back_populates='planet_relationship')

    
class Character(Base):
    __tablename__='character'
    id=Column(Integer,primary_key=True)
    character_id=Column(String(50))
    favorites_characters= relationship('Favorites_characters',back_populates='character_relationship')

    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
