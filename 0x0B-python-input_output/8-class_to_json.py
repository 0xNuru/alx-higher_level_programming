#!/usr/bin/python3
"""This module contains function that returns the dict description"""


def class_to_json(obj):
    """
    Desc:
        a function that returns the dict desc with simple data struc
    """
    return obj.__dict__
