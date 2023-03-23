#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", 
                          cascade="all, delete-orphan")

def __init__(self, *args, **kwargs):
    super(self).__init__(*args, **kwargs)

def cities(self):
    from models import storage
    st_cities = []
    for city in storage.all("City").values():
        if city.state_id == self.id:
            st_cities.append(city)
    return st_cities