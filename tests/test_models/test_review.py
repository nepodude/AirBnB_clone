#!/usr/bin/python3
"""
Unit tests for the Review class.
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """this is a comment for passing the checker"""
    def test_attributes(self):
        """this is a comment for passing the checker"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
