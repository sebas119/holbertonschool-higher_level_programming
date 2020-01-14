#!/usr/bin/python3
class Rectangle(object):

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):

        if (self.__height is 0 or self.__width is 0):
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):

        if (self.__height is 0 or self.__width is 0):
            return ''
        ans = ""
        for i in range(self.__height):
            for j in range(self.__width):
                ans += '#'
            if (self.__height - 1 != i):
                ans += '\n'
        return ans

    def __repr__(self):
        return "Rectangle({},{})".format(self.__width, self.__height)
