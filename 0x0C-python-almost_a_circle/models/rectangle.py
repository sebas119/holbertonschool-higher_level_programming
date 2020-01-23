#!/usr/bin/python3

"""Defines a class Rectangle."""

from models.base import Base


class Rectangle(Base):
    """Represent a Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width attribute."""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Get height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set height attribute."""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Get x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x attribute."""

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y attribute."""

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area Rectangle"""

        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for k in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """String representation of the class"""

        return "[Rectangle] ({}) {}/{} - <{}>/<{}>".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )
