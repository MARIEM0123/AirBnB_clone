#!/usr/bin/python3
"""Heritates from BaseModel the State class."""
from models.base_model import BaseModel

class State(BaseModel):
    """Definition of the class of a state.

    Attributes:
        name (str): string - empty string the name of the state.
    """

    name = ""
