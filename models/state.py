#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if type(DBStorage) == type(FileStorage):
        cities = relationship("City", back_populates="state")
    @property
    def cities(self):
        """cities in FileStorage"""
        cit = []
        for c in storage.all(City).values():
            if c.state_id == self.id:
                cit.append(c)
        return cit
