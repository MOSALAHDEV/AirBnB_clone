#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    classes = {
        "BaseModel": BaseModel, "User": User,
        "State": State, "City": City,
        "Amenity": Amenity, "Place": Place,
        "Review": Review
    }

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        objects_dict = {}
        for key, obj in self.__objects.items():
            objects_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(objects_dict, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                objects_dict = json.load(f)
            for key, value in objects_dict.items():
                class_name = value.get("__class__", None)
                if class_name == "BaseModel":
                    self.__objects[key] = BaseModel(**value)
                elif class_name == "User":
                    self.__objects[key] = User(**value)
                elif class_name == "State":
                    self.__objects[key] = State(**value)
                elif class_name == "City":
                    self.__objects[key] = City(**value)
                elif class_name == "Amenity":
                    self.__objects[key] = Amenity(**value)
                elif class_name == "Place":
                    self.__objects[key] = Place(**value)
                elif class_name == "Review":
                    self.__objects[key] = Review(**value)
                else:
                    pass
        except FileNotFoundError:
            pass
