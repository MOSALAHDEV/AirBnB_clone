#!/usr/bin/python3
" This module contains the Amenity class"
from models.base_model import BaseModel
from models import amenity
import unittest


class TestAmenity(unittest.TestCase):
    """ This class contains unit tests for the Amenity class"""

    def test_init(self):
        """ Test init method """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity.name, str)


if __name__ == '__main__':
    unittest.main()
