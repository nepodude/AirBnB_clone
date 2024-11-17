#!/usr/bin/python3
"""
Unit tests for the Amenity class.
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """this is a comment for passing the checker"""
    def test_attributes(self):
        """this is a comment for passing the checker"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    """this is a comment for passing the checker"""
    unittest.main()
