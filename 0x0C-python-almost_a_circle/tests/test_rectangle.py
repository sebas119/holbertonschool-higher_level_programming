#!/usr/bin/python3

"""Defines a class TestRectangleMethods for testing purposes"""

from models.rectangle import Rectangle
from models.base import Base
import unittest
import sys
import io


class TestRectangleMethods(unittest.TestCase):

    def test_init_with_parameter(self):
        """
        Check if all that obj affects the attribute id
        of the parent class base
        """

        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r3.id, 3)
        Base._Base__nb_objects = 0

    def test_init_rect_with_parameter_id(self):
        """
        Check if the last parameter id is working on Base
        """

        r1 = Rectangle(1, 2, 3, 4, 10)
        self.assertEqual(r1.id, 10)
        Base._Base__nb_objects = 0

    def test_is_instance(self):
        """
        Check if the obj is instance of Rectangle and
        subclass of Base
        """

        r1 = Rectangle(2, 10)
        self.assertIsInstance(r1, (Rectangle, Base))
        Base._Base__nb_objects = 0

    def test_attributes_setter_validation(self):
        """
        Check if the attributes are validated in the setter
        """

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "1")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_area_value(self):
        """
        Check the area of the Rectangle
        """

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display_rectangle_4_6(self):
        """
        Check the display method
        """

        capture = io.StringIO()
        sys.stdout = capture
        r1 = Rectangle(4, 6)
        r1.display()
        out = capture.getvalue()
        sys.stdout = sys.__stdout__
        display = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, out)

    def test_display_rectangle_2_2(self):
        """
        Check the display method
        """

        capture = io.StringIO()
        sys.stdout = capture
        r1 = Rectangle(2, 2)
        r1.display()
        out = capture.getvalue()
        sys.stdout = sys.__stdout__
        display = "##\n##\n"
        self.assertEqual(display, out)

    def test_display_rectangle_2_3_2_2(self):
        """
        Check the display method
        """

        capture = io.StringIO()
        sys.stdout = capture
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        out = capture.getvalue()
        sys.stdout = sys.__stdout__
        display = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(display, out)

    def test_display_rectangle_3_2_1_0(self):
        """
        Check the display method
        """

        capture = io.StringIO()
        sys.stdout = capture
        r1 = Rectangle(3, 2, 1, 0)
        r1.display()
        out = capture.getvalue()
        sys.stdout = sys.__stdout__
        display = " ###\n ###\n"
        self.assertEqual(display, out)

    def test_display_rectangle_str_1(self):
        """
        Check the display method
        """

        capture = io.StringIO()
        sys.stdout = capture
        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)
        out = capture.getvalue()
        sys.stdout = sys.__stdout__
        display = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(display, out)

    def test_display_rectangle_str_2(self):
        """
        Check the display method
        """

        capture = io.StringIO()
        sys.stdout = capture
        r1 = Rectangle(5, 5, 1)
        print(r1)
        out = capture.getvalue()
        sys.stdout = sys.__stdout__
        display = "[Rectangle] (11) 1/0 - 5/5\n"
        self.assertEqual(display, out)
