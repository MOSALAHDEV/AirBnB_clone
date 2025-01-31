#!/usr/bin/python3
"""This module contains the City class"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for city class"""
    def test_class(self):
        self.assertEqual(city.__class__, City)
        self.assertEqual(city.__base__, BaseModel)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
