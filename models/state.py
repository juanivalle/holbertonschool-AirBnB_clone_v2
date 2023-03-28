#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")

    if (getenv("HBNB_TYPE_STORAGE") != "db"):
        @property
        def cities(self):
            from models import storage
            st_cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    st_cities.append(city)
            return st_cities
