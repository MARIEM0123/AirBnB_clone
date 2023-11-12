#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """The class for abstracted storage of data in Json format.

    Attributes:
        __file_path (str): The path to the Json file.
        __objects (dict): A dictionary to store objects by <class_name>.id.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add obj in __objects with key <obj_class_name>.id"""
        ocn = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocn, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        objdt = FileStorage.__objects
        objdict = {obj: objdt[obj].to_dict() for obj in objdt.keys()}
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(objdict, json_file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path)"""
        try:
            with open(FileStorage.__file_path) as json_file:
                objdt = json.load(json_file)
                for a in objdt.values():
                    class_nm = a["__class__"]
                    del a["__class__"]
                    self.new(eval(class_nm)(**a))
        except FileNotFoundError:
            return
