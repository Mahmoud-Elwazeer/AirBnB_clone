#!/usr/bin/python3
"""user sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """sub class that inherit from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def __str__(self):
    #     return f"{self.__class__.__name__}"
