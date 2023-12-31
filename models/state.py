#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

from sqlalchemy.orm import relationship
import os

Base = declarative_base()
env_v = os.environ.get('HBNB_TYPE_STORAGE')


from models import storage
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    if env_v == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            from models.city import City
            obj_list = []
            stor = storage.all(City)
            for key, value in stor.items():
                if self.id == value.state_id:
                    obj_list.append(value)
            return obj_list
