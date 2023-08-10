#!/usr/bin/python3
"""module used for testing basemodel
"""
from models import base_model
import unittest


class TestBaseModel(unittest.TestCase):
    """test cases for basemodel class
    """

    def test_module_documetation(self):
        """test the documentation of a module"""
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class_documetation(self):
        """test the documentation of class"""
        self.assertTrue(len(base_model.BaseModel.__doc__) > 0)

    def test_method_documetation(self):
        """test documentation of methods inside and outside class"""
        for method in dir(base_model.BaseModel):
            self.assertTrue(len(method.__doc__) > 0)

    def test_str_method(self):
        """testing __str__ representation"""
        b = base_model.BaseModel()
        expected_output = f"[BaseModel] ({b.id}) {b.__dict__}"
        self.assertEqual(b.__str__(), expected_output)
