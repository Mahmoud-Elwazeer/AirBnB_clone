#!/usr/bin/python3
"""Storage module for storing the date as JSON format
"""
from models.base_model import BaseModel
import json


class FileStorage:
    """class sued for serialization and deserialization
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        # self.__objects[key] = obj
        # key = <obj class name>.id
        # classname.id  ->     ERROR
        # object.id    -> correct
        # key = obj className + object.id ==> className.id

        # class_name = __class__.__name__
        # self.__objects[obj.class_name.id] = obj

        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, mode='w', encoding='utf-8') as fp:
            json.dump(self.__objects, fp, indent=4)

    def reload(self):
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as fp:
                py_object = json.load(fp)
        except FileNotFoundError:
            pass
