#!/usr/bin/python3
"""
Unit tests for the State class.
"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """
    Test suite for the State class.
    """

    def test_attributes(self):
        """
        Test that the default attributes of a State instance are initialized correctly.
        """
        state = State()
        self.assertEqual(state.name, "")

if __name__ == "__main__":
    """
    Execute the unit tests when the file is run as a script.
    """
    unittest.main()
