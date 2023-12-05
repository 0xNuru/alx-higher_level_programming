#!/usr/bin/python3
"""This module contains a function that produces JSON representation"""
import json


def to_json_string(my_obj):
    """
    Desc:
        a function that returns the JSON repr of an obj
    Returns:
        JSON repr
    """
    return json.dumps(my_obj)
