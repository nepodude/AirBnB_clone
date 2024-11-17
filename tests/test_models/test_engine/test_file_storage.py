#!/usr/bin/python3
"""
Unit tests for FileStorage class
"""


import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path
        self.obj = BaseModel()

    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method(self):
        """Test the `all` method returns a dictionary"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_method(self):
        """Test the `new` method adds an object"""
        key = f"BaseModel.{self.obj.id}"
        self.storage.new(self.obj)
        self.assertIn(key, self.storage.all())

    def test_save_method(self):
        """Test the `save` method writes to the JSON file"""
        self.storage.new(self.obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, "r") as f:
            data = json.load(f)
        key = f"BaseModel.{self.obj.id}"
        self.assertIn(key, data)

    def test_reload_method(self):
        """Test the `reload` method restores objects"""
        self.storage.new(self.obj)
        self.storage.save()
        self.storage.reload()
        key = f"BaseModel.{self.obj.id}"
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
