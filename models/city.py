#!/usr/bin/python3
"""The class heritate from BaseModal City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Definition of the class city a city.

    Attributes:
        state_id (str): string - empty string: it will be the State.id.
        name (str):string - empty stringtThe name of the city.
    """

    state_id = ""
    name = ""
