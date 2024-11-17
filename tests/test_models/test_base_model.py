#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
"""
Unittest for the BaseModel class
This module tests the functionality of the BaseModel class, including:
- Instance creation
- Dictionary representation
- Save method for updating timestamps
"""


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class
    """
    def test_instance_creation(self):
        """
        Test if an instance of BaseModel is created correctly.
        Checks:
        - The instance is of type BaseModel.
        - The 'id' attribute is a string.
        - 'created_at' and 'updated_at' are datetime objects.
        """
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel.
        Checks:
        - The returned dictionary contains the '__class__' key.
        - The '__class__' key's value is the class name 'BaseModel'.
        - The 'id' in the dictionary matches the instance's 'id'.
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIn("__class__", obj_dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["id"], obj.id)

    def test_save_method(self):
        """
        Test the save method of BaseModel.
        Checks:
        - The 'updated_at' attribute changes after calling save().
        """
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, old_updated_at)


if __name__ == "__main__":
    """
    Run all the test cases when the script is executed.
    """
    unittest.main()
