#!/usr/bin/python3
"""This module contains a function to add two ints"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the sum.

    Args:
        a: The first integer.
        b: The second integer (default: 98).

    Raises:
        TypeError: If either `a` or `b` is not an integer.

    Returns:
        The sum of `a` and `b`.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
