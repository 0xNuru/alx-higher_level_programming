#!/usr/bin/python3
"""This module contains a funciton that creates an object"""
import json


def load_from_json_file(filename):
    """
    Desc:
        a function that creates an Object from a “JSON file”
    """
    with open(filename) as f:
        data = json.load(f)
        return data
