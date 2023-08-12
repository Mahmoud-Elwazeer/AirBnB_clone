#!/usr/bin/python3
"""module used for testing basemodel
"""
from models import base_model
import unittest
from datetime import datetime

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

    def test_init(self):
        """test create object from BaseModel"""
        my_model = base_model.BaseModel()
        self.assertIsInstance(my_model , base_model.BaseModel)
    
    def test_str_id(self):
        """test id -> str"""
        my_model = base_model.BaseModel()
        self.assertIsInstance(my_model.id, str)

    def test_datatime_created_at(self):
        """test created_at -> datetime"""
        my_model = base_model.BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)

    def test_datatime_updated_at(self):
        """test updated_at -> datetime"""
        my_model = base_model.BaseModel()
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str_method(self):
        """testing __str__ representation"""
        my_model = base_model.BaseModel()
        utput = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(my_model.__str__(), utput)

    def test_unique_id(self):
        """test if the id is unique"""
        b1 = base_model.BaseModel()
        b2 = base_model.BaseModel()

        self.assertNotEqual(b1.id, b2.id)
