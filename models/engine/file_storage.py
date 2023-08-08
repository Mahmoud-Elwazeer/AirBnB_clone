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
        class_name = __class__.__name__
        FileStorage.__objects[__class__.__name__] = obj
        self.__objects[obj.class_name.id] = obj

    def save(self):
        with open(self.__file_path, mode='w', encoding='utf-8') as fp:
            json.dump(self.__objects, fp, indent=4)

    def reload(self):
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as fp:
                py_object = json.load(fp)
        except FileNotFoundError:
            pass
