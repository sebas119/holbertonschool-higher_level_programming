#!/usr/bin/python3

from models.base import Base
import unittest


class TestBaseMethods(unittest.TestCase):

    def test_init_base_with_parameter(self):

        b1 = Base(1)
        self.assertEqual(b1.id, 1)
        Base._Base__nb_objects = 0

    def test_init_base_without_parameter(self):

        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, 3)
        Base._Base__nb_objects = 0

    def test_init_base_with_none(self):

        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)
        Base._Base__nb_objects = 0
