#!/usr/bin/python3
"""module used for testing User
"""
from models import user
import unittest


class TestBaseModel(unittest.TestCase):
    """test cases for user class
    """

    def test_module_documetation(self):
        """test the documentation of a module"""
        self.assertTrue(len(user.__doc__) > 0)

    def test_class_documetation(self):
        """test the documentation of class"""
        self.assertTrue(len(user.BaseModel.__doc__) > 0)

    def test_method_documetation(self):
        """test documentation of methods inside and outside class"""
        for method in dir(user.BaseModel):
            self.assertTrue(len(method.__doc__) > 0)

    def test_str_method(self):
        """testing __str__ representation"""
        b = user.BaseModel()
        expected_output = f"[BaseModel] ({b.id}) {b.__dict__}"
        self.assertEqual(b.__str__(), expected_output)

    def test_unique_id(self):
        """test if the id is unique"""
        u1 = user.BaseModel()
        u2 = user.BaseModel()
        self.assertNotEqual(u1.id, u2.id)
