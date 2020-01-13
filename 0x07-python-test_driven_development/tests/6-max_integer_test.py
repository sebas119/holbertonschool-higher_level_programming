#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_is_integer(self):
        self.assertNotIsInstance(max_integer([2, 8.5]), int)
