#!/usr/bin/python3
"""comments"""

from models.user import User
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import getenv

mod = {"City": City, "State": State, "User": User,
       "Amenity": Amenity, "Place": Place, "Review": Review}


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(('mysql+mysqldb://{}:{}@{}/{}')
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                              pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        objects = {}
        for clas in mod:
            if mod[clas] == cls or cls is None:
                for key in self.__session.query(mod[clas]).all():
                    key = "{}.{}".format(__name__+'.'+key.id)
        return objects

    def new(self, obj):
        """comments"""
        self.__session.add(obj)

    def save(self):
        """comments"""
        self.__session.commit()

    def delete(self, obj=None):
        """comments"""
        self.__session.delete(obj)

    def reload(self):
        """comments"""
        Base.metadata.create_all(self.__engine)
        ssession = sessionmaker(bind=self.__engine, expire_on_commit=False)
        ssession = scoped_session(ssession)
        self.__session = ssession

    def close(self):
        """comments"""
        self.__session.close()
