#!/usr/bin/python3
"""module has BaseModule"""
import uuid
from datetime import datetime
import json


class BaseModel:
    """BaseModel that defines all common attributes/methods
    for other classes
    """

    def __init__(self):
        """init magic method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string representation of instance
        """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        class_name = __class__.__name__
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__["__class__"] = class_name
        return self.__dict__
        # # return (json.dumps(self.__dict__))
        # return f"{self.__dict__}"

        # for key, value in self.__dict__.items():
        #     if key == "created_at" or key == "updated_at":
        #         self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        #         self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")


my_model_json = BaseModel().to_dict()
print(my_model_json)
