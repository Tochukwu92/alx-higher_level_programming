#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class."""

    def test_max_integer(self):
        """test for max. integer."""

        self.list1 = [2,8,0,5, 3]
        self.list2 = [2.7, 3, 8.6, 7]
        self.list3 = [2, 5, 'school', 6]
        self.list4 = [8, 10, 6 + 7j, 2]
        self.list5 = [8, 7, 2, True, 7]
        self.list6 = [12, 7, 12, 6, 1]
        self.list7 = []
        self.assertEqual(max_integer(self.list1), 8)
        self.assertEqual(max_integer(self.list6), 12)
        self.assertEqual(max_integer(self.list7), None)
        with self.assertRaises(TypeError):
            max_integer(self.list3)
            max_integer(self.list5)
