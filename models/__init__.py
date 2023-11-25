#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

var = "HBNB_TYPE_STORAGE"
env_v = os.environ.get(var)

if env_v =="db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
