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
    super().__init__(*args, **kwargs)

def cities(self):
    from models import storage
    st_cities = []
    for val in storage.all("City").values():
        if val.state_id == self.id:
            st_cities.append(val)
    return st_cities