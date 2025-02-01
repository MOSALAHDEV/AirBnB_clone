#!/usr/bin/python3
" This module contains unit tests for the State class"
import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """ This class contains unit tests for the State class"""

    def test_init(self):
        """ Test init method """
        state = State()
        self.assertEqual(state.__class__, State)
        self.assertIsInstance(state, BaseModel)
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
