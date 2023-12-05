#!/usr/bin/python3
"""This module contains a function that writes to a  text file"""


def write_file(filename="", text=""):
    """
    Desc:
        a function that writes to a text file (UTF8)
    Args:
        filename (file): path of the file opened
    Return:
        the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        count = f.write(text)

        return count
