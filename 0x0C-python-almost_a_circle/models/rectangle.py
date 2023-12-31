#!/usr/bin/python3
"""This module contains Rectangle class"""

from base import Base


class Rectangle(Base):
    """This class defines rectangle objects"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializatin of variables"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width
    @width.setter
    def width(self, value):
        """setter for width"""
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height
    @height.setter
    def height(self, value):
        """setter for height"""
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x
    @wx.setter
    def x(self, value):
        """setter for x"""
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y
    @y.setter
    def y(self, value):
        """setter for y"""
        self.__y = value

