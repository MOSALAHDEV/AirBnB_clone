#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    classes = {"BaseModel": BaseModel, "User": User}

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
                else:
                    pass
        except FileNotFoundError:
            pass
