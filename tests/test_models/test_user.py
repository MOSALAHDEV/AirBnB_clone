#!/usr/bin/python3
"""This module contains unit tests for the User class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """This class contains unit tests for the User class"""
    def test_init(self):
        """Test init method"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)


if __name__ == '__main__':
    unittest.main()
