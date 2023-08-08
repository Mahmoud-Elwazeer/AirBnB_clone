#!/usr/bin/python3
"""module has BaseModule"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel that defines all common attributes/methods
    for other classes
    """

    def __init__(self):
        """init magic method"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """string representation of instance
        """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()


b = BaseModel()
print(b.id)
# print()
b.save()
# print()
print(b)
