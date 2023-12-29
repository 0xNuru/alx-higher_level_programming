#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        """Test for empty list"""
        self.assertIsNone(max_integer([]))

    def test_int_list(self):
        """Test a normal list"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

        #test negative ints
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

        result = max_integer([-1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_float(self):
        """Test float list"""
        result = max_integer([1.0, 2.5, 8.8, 3.9, 4.2])
        self.assertEqual(result, 8.8)

        #test negative float
        result = max_integer([-1.9, -2.3, -3.2, -4.1])
        self.assertEqual(result, -1.9)

    def test_char(self):
        """Test with chars"""
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')

    def test_strings(self):
        """Test with strings"""
        self.assertEqual(max_integer(['art', 'bat', 'cat', 'dart']), 'dart')
        self.assertEqual(max_integer('Nuru'), 'u')

    def test_int_list(self):
        """Test singleton"""
        result = max_integer([4])
        self.assertEqual(result, 4)






if __name__ == "__main__":
    unittest.main()


