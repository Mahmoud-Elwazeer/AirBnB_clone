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
