#!/usr/bin/python3
"""Heritates from BaseModel a Review class."""
from models.base_model import BaseModel

class Review(BaseModel):
    """Definition of a review

    Attributes:
        place_id (str): string - empty string: it will be the Place.id
        user_id (str): string - empty string: it will be the User.id
        text (str): string - empty string
    """

    place_id = ""
    user_id = ""
    text = ""
