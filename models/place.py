#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60),ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(Integer, nullable=False, default=0)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', back_populates='place',
            cascade="all, delete-orphan")
    else:
        @property
        def reviews(self):
            """ Getter for reviews attribute """
            from models import storage
            from models.review import Review
            reviews_dict = storage.all(Review)
            place_reviews = []
            for review in reviews_dict.values():
                if review.place_id == self.id:
                    place_reviews.append(review)
            return place_reviews

    @property
    def amenities(self):
        """ Getter for amenities attribute """
        from models import storage
        from models.amenity import Amenity
        amenities_dict = storage.all(Amenity)
        place_amenities = []
        for amenity in amenities_dict.values():
            if amenity.id in self.amenity_ids:
                place_amenities.append(amenity)
        return place_amenities

    @amenities.setter
    def amenities(self, obj):
        """ Setter for amenities attribute """
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
