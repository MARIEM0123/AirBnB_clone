#!/usr/bin/python3
"""It's the python class model named BaseModel class."""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """It's the BaseModel for other classes in the HBnB cloneproject."""

    def __init__(self, *args, **kwargs):
        """Initialization of the instances ofattributes of the BaseModel class

        Args:
            *args : Not taken into consideration in date code
            **kwargs (dict): Having every Key or value ofgiven  attributes and considering a dictionary
        """
        tmfrmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, tmfrmt)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def save(self):
        """Registers the instance to an updated datetime witch is the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary representing the instances of the BaseModel
        a string representing the timestamp of the instance of the object
        and its class name
        """
        rst_dict = self.__dict__.copy()
        rst_dict["created_at"] = self.created_at.isoformat()
        rst_dict["updated_at"] = self.updated_at.isoformat()
        rst_dict["__class__"] = self.__class__.__name__
        return rst_dict

    def __str__(self):
        """Return the print  representation of the BaseModel instance
	including the name of the class and the timestamp"""
        clsnm = self.__class__.__name__
        return "[{}] ({}) {}".format(clsnm, self.id, self.__dict__)
