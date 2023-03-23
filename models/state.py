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
    """comments"""
    super().__init__(*args, **kwargs)

def cities(self):
    from models import storage
    state_city = []
    for val in storage.all("City").values():
        if self.id == City.state_id:
            state_city.append(storage.all(City)[val])
    return state_city