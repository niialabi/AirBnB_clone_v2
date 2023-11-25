#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey

Base = declarative_base()



class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("state.id"), nullable=False)
