#!/usr/bin/python3
"""This module contains tests for the square class"""

import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """Test Square class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_instance(self):
        """Test if square is an instance of Base"""
        self.assertIsInstance(Square(98), Base)

    def test_inheritance(self):
        """Test if square inherits from Rectangle class"""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_empty_square(self):
        with self.assertRaises(TypeError):
            Square()

    def test_nb_objects_attr(self):
        """Test the private class attribute __nb_objects"""
        self.assertIsNotNone(Base._Base__nb_objects)
        self.assertEqual(Base._Base__nb_objects, 0)
        sq = Square(1, 2)
        Square(11, 22)
        Square(111, 222)
        self.assertEqual(Base._Base__nb_objects, 3)

    def test_excess_constructor_args(self):
        """Tests constructor signature"""
        with self.assertRaises(TypeError) as e:
            sq = Square(1, 2, 3, 4, 5, 6)

    def test_intsance_id(self):
        """test default id"""
        sq1 = Square(10, 20)
        self.assertEqual(sq1.id, 1)

        #test custom id
        sq2 = Square(1, 1, 3, 4)
        self.assertEqual(sq2.id, 4)

        #test three args
        sq3 = Square(10, 20, 3)
        self.assertEqual(sq3.id, 2)



if __name__ == "__main__":
    unittest.main()
