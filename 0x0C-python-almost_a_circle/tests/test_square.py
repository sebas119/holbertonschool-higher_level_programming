#!/usr/bin/python3

"""Defines a class TestSquareMethods for testing purposes"""

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import unittest
import sys
import io


class TestSquareMethods(unittest.TestCase):

    def test_init_with_parameter(self):
        """
        Check if all that obj affects the attribute id
        of the parent class base
        """

        r1 = Square(10, 2)
        r2 = Square(2, 10)
        r3 = Square(10, 2)
        self.assertEqual(r3.id, 3)
        Base._Base__nb_objects = 0

    def test_init_rect_with_parameter_id(self):
        """
        Check if the last parameter id is working on Base
        """

        r1 = Square(1, 2, 3, 10)
        self.assertEqual(r1.id, 10)
        Base._Base__nb_objects = 0

    def test_is_instance(self):
        """
        Check if the obj is instance of Square and
        subclass of Base
        """

        r1 = Square(2, 10)
        self.assertIsInstance(r1, (Rectangle, Square, Base))
        Base._Base__nb_objects = 0

    def test_area_value(self):
        """
        Check the area of the Square
        """

        r1 = Square(3, 2)
        self.assertEqual(r1.area(), 9)

        r2 = Square(2, 10)
        self.assertEqual(r2.area(), 4)

        r3 = Square(8, 7)
        self.assertEqual(r3.area(), 64)
        Base._Base__nb_objects = 0

    def test_display_square_5(self):
        """
        Check the display method
        """

        capture = io.StringIO()
        sys.stdout = capture
        r1 = Square(5)
        r1.display()
        out = capture.getvalue()
        sys.stdout = sys.__stdout__
        display = "#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(display, out)
        Base._Base__nb_objects = 0

    def test_display_square_2_x2(self):
        """
        Check the display method
        """

        capture = io.StringIO()
        sys.stdout = capture
        r1 = Square(2, 2)
        r1.display()
        out = capture.getvalue()
        sys.stdout = sys.__stdout__
        display = "  ##\n  ##\n"
        self.assertEqual(display, out)
        Base._Base__nb_objects = 0

    def test_display_square_3_x1_y3(self):
        """
        Check the display method
        """

        capture = io.StringIO()
        sys.stdout = capture
        r1 = Square(3, 1, 3)
        r1.display()
        out = capture.getvalue()
        sys.stdout = sys.__stdout__
        display = "\n\n\n ###\n ###\n ###\n"
        self.assertEqual(display, out)
        Base._Base__nb_objects = 0

    def test_attributes_setter_validation(self):
        """
        Check if the attributes are validated in the setter
        """

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Square(10)
            r.size = -10
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square(10, 2)
            r.size = {}

        Base._Base__nb_objects = 0

    def test_square_update_args_1(self):
        """
        Check the update method with args
        """

        capture = io.StringIO()
        sys.stdout = capture
        r1 = Square(5)
        r1.update(10)
        print(r1)
        out = capture.getvalue()
        sys.stdout = sys.__stdout__
        display = "[Square] (10) 0/0 - 5\n"
        self.assertEqual(display, out)
        Base._Base__nb_objects = 0

    def test_square_update_kwargs_1(self):
        """
        Check the update method with kwargs
        """

        capture = io.StringIO()
        sys.stdout = capture
        r1 = Square(1, 2, 3, 4)
        r1.update(x=12)
        print(r1)
        out = capture.getvalue()
        sys.stdout = sys.__stdout__
        display = "[Square] (4) 12/3 - 1\n"
        self.assertEqual(display, out)
        Base._Base__nb_objects = 0
