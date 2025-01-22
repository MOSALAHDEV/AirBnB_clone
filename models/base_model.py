#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models

"""
This module contains the BaseModel class
"""

class BaseModel:
    """
    This class defines all common attributes/methods for other classes
    """

    def __init__(self):
        """
        Initializes the BaseModel instance
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
