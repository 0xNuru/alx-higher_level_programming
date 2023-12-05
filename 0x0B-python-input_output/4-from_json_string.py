#!/usr/bin/python3
"""This module contains a functin that converts JSON to obj"""
import json


def from_json_string(my_str):
    """
    Desc:
        this function converts JSON to object
    Args:
        my_str (str): JSON to be converted
    """
    return json.loads(my_str)
