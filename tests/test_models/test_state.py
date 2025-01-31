#!/usr/bin/python3
" This module contains unit tests for the State class"
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ This class contains unit tests for the State class"""

    def test_init(self):
        """ Test init method """
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state.name, str)


if __name__ == '__main__':
    unittest.main()
