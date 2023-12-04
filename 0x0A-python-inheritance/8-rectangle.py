#!/usr/bin/python3
"""This module contains a Rectangle class that inherits from BaseGeo"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A cls that defines the rect instance"""
    def __init__(self, width, height):
        """A method to construct the rect"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
