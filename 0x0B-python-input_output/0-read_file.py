#!/usr/bin/python3
"""This module contains a function that reads from a text file"""


def read_file(filename=""):
    """
    Desc:
        a function that reads a text file (UTF8)
        and prints it to stdout
    Args:
        filename (file): path of the file opened
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
