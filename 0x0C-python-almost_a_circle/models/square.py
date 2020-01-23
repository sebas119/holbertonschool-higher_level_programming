#!/usr/bin/python3

"""Defines a class Square."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size attribute"""

        return self.width

    @size.setter
    def size(self, value):
        """Set size attribute."""

        self.width = value
        self.height = value

    def __str__(self):
        """String representation of the class"""

        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )
