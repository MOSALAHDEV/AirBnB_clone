#!/usr/bin/python3
"""This module test cases contain the Place class"""
from models.base_model import BaseModel
from models import place
import unittest


class TestPlace(unittest.TestCase):
    """Test cases for place class"""
    def test_class(self):
        self.assertEqual(place.__class__, Place)
        self.assertEqual(place.__base__, BaseModel)
        self.assertEqual(type(place.city_id), str)
        self.assertEqual(type(place.user_id), str)
        self.assertEqual(type(place.name), str)
        self.assertEqual(type(place.description), str)
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(type(place.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
