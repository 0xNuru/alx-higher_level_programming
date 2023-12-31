#!/usr/bin/env python3
"""Unit test for the base class"""

import unittest
from models.base import Base



class TestBaseClass(unittest.TestCase):
    """Test the Base class"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_nb_objects_attr(self):
        """Test the private class attribute __nb_objects"""
        self.assertIsNotNone(Base._Base__nb_objects)
        self.assertEqual(Base._Base__nb_objects, 0)
        Base()
        Base()
        Base()
        self.assertEqual(Base._Base__nb_objects, 3)
    
    def test_default_id(self):
        """Test the instantiation of a base object with no given id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id(self):
        """Test when id is provided"""
        b1 = Base()
        b2 = Base(99)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 99)
        self.assertEqual(b3.id, 2)

    def test_init_with_zero_id(self):
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_init_with_negative_id(self):
        b1 = Base(-5)
        self.assertEqual(b1.id, -5)

    def test_init_with_large_id(self):
        b1 = Base(10**6)
        self.assertEqual(b1.id, 10**6)

    def test_kwargs(self):
        b1 = Base(id=99)
        self.assertEqual(b1.id, 99)
    
    def test_none(self):
        b1 = Base(None)
        self.assertEqual(b1.id, 1)
    
    def mod_id(self):
        b1 = Base(2)
        b1.id = 99
        self.assertEqual(b1.id, 99)
    
    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)


if __name__ == "__main__":
    unittest.main()
