#!/usr/bin/python3
"""the __init__ module
"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
