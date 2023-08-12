#!/usr/bin/python3
"""Module for file_storage test Cases
"""
from models.engine import file_storage
import unittest


class TestFileStorage(unittest.TestCase):
    """test cases for FileStorage class
    """

    def test_module_documetation(self):
        """test the documentation of a module
        """
        self.assertTrue(len(file_storage.__doc__) > 0)

    def test_class_documetation(self):
        """test the documentation of class
        """
        self.assertTrue(len(file_storage.FileStorage.__doc__) > 0)

    def test_method_documetation(self):
        """test documentation of methods inside and outside class
        """
        for method in dir(file_storage):
            self.assertTrue(len(method.__doc__) > 0)

    def test_all_method(self):
        """test the return type of all method
        """
        f = file_storage.FileStorage()
        self.assertEqual(type(f.all()), dict)
