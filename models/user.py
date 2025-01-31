#!/usr/bin/python3
""" This module defines a User class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """ This class represents a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
