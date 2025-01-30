#!/usr/bin/python3
"""
unit tests for the FileStorage class
"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class
    """

    def setUp(self):
        """
        Set up the test environment
        """
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path
        self.objects = self.storage._FileStorage__objects
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """
        Tear down the test environment
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """
        Test the all method
        """
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(objects, {})

    def test_save(self):
        """
        Test the save method
        """
        model = BaseModel()
        key = f"{model.__class__.__name__}.{model.id}"
        self.storage.new(model)
        self.storage.save()
        self.assertIn(key, self.storage.all())
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """
        Test the reload method
        """
        model = BaseModel()
        key = f"{model.__class__.__name__}.{model.id}"
        self.storage.new(model)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], BaseModel)


if __name__ == '__main__':
    unittest.main()
