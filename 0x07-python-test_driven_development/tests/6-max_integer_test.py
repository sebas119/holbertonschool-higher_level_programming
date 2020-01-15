#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertIsNone(max_integer([]))
        self.assertNotIsInstance(max_integer([2, 8.5]), int)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([0, 0]), 0)
        self.assertEqual(max_integer([29]), 29)
        self.assertEqual(max_integer([1, 2, -6]), 2)
        self.assertEqual(max_integer([8, -6, -1, -7]), 8)
        self.assertEqual(max_integer([-29, -80, -100]), -29)
