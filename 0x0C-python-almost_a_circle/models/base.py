#!/usr/bin/python3
"""This module contains a Base class"""
import json

class Base:
    """This is a Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """the JSON string repr of a list of dicts"""
        if list_dictionaries is None  or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
