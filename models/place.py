#!/usr/bin/python3
"""Heritate from BaseModel the Place class."""
from models.base_model import BaseModel

class Place(BaseModel):
    """Definition of  a place class

    Attributes:
        city_id (str): string - empty string: it will be the City.id
        user_id (str): string - empty string: it will be the User.id
        name (str): string - empty string the name of the place
        description (str):  string - empty string represents a place.
        number_rooms (int):  integer - 0 The number of rooms
        number_bathrooms (int):  integer - 0 The number of bathrooms of the place.
        max_guest (int):  integer - 0 The maximum number of guests of the place.
        price_by_night (int):  integer - 0 The price by night of the place.
        latitude (float): Float The latitude of the place.
        longitude (float): Float The longitude of the place.
        amenity_ids (list): list of string - empty list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
