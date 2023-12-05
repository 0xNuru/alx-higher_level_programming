#!/usr/bin/python3
"""This module contains a func that writes a jsonified obj to file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Desc:
        a function that writes an Object to a 
        text file, using a JSON representation
    Args:
        obj (str): the string to be converted to json and then wrtten
        filename (path) the file to be written to
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
