import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    created_at = Column(String(250), nullable=False)
    updated_at = Column(String(250), nullable=True)

class Planets(Base):
    __tablename__ = 'planets'
   
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)
    planet_climate = Column(String(250), nullable=True)
    planet_diameter = Column(Integer, nullable=True)
    planet_population = Column(Integer, nullable=True)
    planet_gravity = Column(Integer, nullable=True)
    planet_terrain = Column(String(250), nullable=True)
    planet_url = Column(String(250), nullable=True)

class Characters(Base):
    __tablename__ = 'characters'
   
    id = Column(Integer, primary_key=True)
    characters_name = Column(String(250), nullable=False)
    characters_gender = Column(String(250), nullable=True)
    characters_birthyear = Column(String(250), nullable=True)
    characters_eyecolor = Column(String(250), nullable=True)
    characters_haircolor = Column(String(250), nullable=True)
    characters_homeworld = Column(String(250), nullable=True)
    characters_height = Column(Integer, nullable=True)
    planet_url = Column(String(250), nullable=True)

class User_Favorites(Base):
    __tablename__ = 'user_favorites'
   
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    planets_id = Column (Integer, ForeignKey('planets.id'))

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')