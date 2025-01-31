#!/usr/bin/python3
"""This module test cases contain the Review class"""
from models.base_model import BaseModel
from models import review
import unittest


class TestReview(unittest.TestCase):
    """Test cases for review class"""
    def test_class(self):
        self.assertEqual(review.__class__, Review)
        self.assertEqual(review.__base__, BaseModel)
        self.assertEqual(type(review.place_id), str)
        self.assertEqual(type(review.user_id), str)
        self.assertEqual(type(review.text), str)


if __name__ == '__main__':
    unittest.main()
