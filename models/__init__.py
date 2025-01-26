#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
