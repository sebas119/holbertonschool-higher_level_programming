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

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

    def update(self, *args, **kwargs):
        """
        Update the attributes values

        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """

        if args is not None and len(args) > 0:
            n = 1
            for arg in args:
                if n == 1:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif n == 2:
                    self.width = arg
                elif n == 3:
                    self.height = arg
                elif n == 4:
                    self.x = arg
                elif n == 5:
                    self.y = arg
                n += 1
        else:
            if kwargs is None:
                return
            for key, value in kwargs.items():

                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle

        This dictionary must contain:
        id
        width
        height
        x
        y
        """

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
