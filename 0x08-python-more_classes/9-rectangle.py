#!/usr/bin/python3

"""This module contains the class Rectangle"""


class Rectangle(object):
    """Representation of a Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Construct method"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Get area of Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Get perimeter of Rectangle"""
        if (self.__height is 0 or self.__width is 0):
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """String representation of Rectangle"""
        if (self.__height is 0 or self.__width is 0):
            return ''
        ans = ""
        for i in range(self.__height):
            for j in range(self.__width):
                ans += str(self.print_symbol)
            if (self.__height - 1 != i):
                ans += '\n'
        return ans

    def __repr__(self):
        """String representation of the specified instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor method"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two Rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Alternative constructor for squares"""
        width, heigth = size, size
        return cls(width, heigth)
