import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class User(Base):
    __tablename__ = 'user'
    email = Column(Integer, primary_key=True)
    password = Column(String(250), nullable=False)
    suscription_date = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    # FK
    user_email = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    film_id = Column(Integer, ForeignKey('film.id'))


class Character(Base):
    __tablename__ ='character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    homeWorld = Column(String(250), nullable=False)
    user_email = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    # FK
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    film_id = Column(Integer, ForeignKey('film.id'))
    
class Film(Base):
    __tablename__= 'film'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    episode = Column(Integer)
    director = Column(String(250), nullable=False)
    productor = Column(String(250), nullable=False)
    # FK
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    user_email = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
