#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship('Place', back_populates='city')
    else:
        @property
        def places(self):
            """ Getter for places attribute """
            from models import storage
            from models.place import Place
            places_dict = storage.all(Place)
            city_places = []
            for place in places_dict.values():
                if place.city_id == self.id:
                    city_places.append(place)
            return city_places
