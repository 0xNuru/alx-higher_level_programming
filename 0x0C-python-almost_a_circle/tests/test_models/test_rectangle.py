#!/usr/bin/python3
"""This module contains tests for the rectangle class"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """Test Rectangle Class"""
    
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_isinstance(self):
        self.assertIsInstance(Rectangle(98, 99), Base)

    def test_empty_rect(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_no_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_nb_objects_attr(self):
        """Test the private class attribute __nb_objects"""
        self.assertIsNotNone(Base._Base__nb_objects)
        self.assertEqual(Base._Base__nb_objects, 0)
        r1 = Rectangle(1, 2)
        Rectangle(11, 22)
        Rectangle(111, 222)
        self.assertEqual(Base._Base__nb_objects, 3)

    def test_intsance_id(self):
        """test default id"""
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.id, 1)

        #test custom id
        r2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r2.id, 5)

        #test three args
        r3 = Rectangle(10, 20, 1)
        self.assertEqual(r3.x, 1)

    def test_privacy(self):
        with self.assertRaises(AttributeError):
            width = Rectangle(10, 20, 1, 2, 99).__width

        with self.assertRaises(AttributeError):
            height = Rectangle(10, 20, 1, 2, 99).__height

        with self.assertRaises(AttributeError):
            x = Rectangle(10, 20, 1, 2, 9).__x

        with self.assertRaises(AttributeError):
            y = Rectangle(10, 20, 1, 2, 9).__y

    def test_getters(self):
        r1 = Rectangle(10, 20, 1, 2, 99)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)

    def test_setters(self):
        r1 = Rectangle(10, 20, 1, 2, 99)
        r1.width = 100
        self.assertEqual(r1.width, 100)
        r1.height = 200
        self.assertEqual(r1.height, 200)
        r1.x = 10
        self.assertEqual(r1.x, 10)
        r1.y = 20
        self.assertEqual(r1.y, 20)

    def test_kwargs_instance(self):
        r1 = Rectangle(width=10, height=20, x=3, y=4)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_args_instance(self):
        r1 = Rectangle(10, 20, 3, 4)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
