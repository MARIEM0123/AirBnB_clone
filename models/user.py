#!/usr/bin/python3
"""Heritates from BaseModel for the User class."""
from models.base_model import BaseModel

class User(BaseModel):
    """Defines a User model.

    Attributes:
        email (str): string - empty string the email of the user.
        password (str): string - empty string the password of the user.
        first_name (str): string - empty string the first name of the user.
        last_name (str): string - empty string the last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
