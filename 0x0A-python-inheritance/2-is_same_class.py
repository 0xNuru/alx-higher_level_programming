#!/usr/python3
"""This module contains a function that returns true if an object is an
instance of a specified class"""


def is_same_class(obj, a_class):
    """A function to check isinstance"""
    return type(obj) == a_class
