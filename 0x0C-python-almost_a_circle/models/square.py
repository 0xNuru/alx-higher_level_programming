#!/usr/bin/python3
"""This module contains the Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines the rectangle object"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of square
            x (int): The x coordinate of the sq
            y (int): The y coordinate of the sq
            id (int): The id of the sq
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override str representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
