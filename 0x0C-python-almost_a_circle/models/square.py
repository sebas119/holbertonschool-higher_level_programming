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

    def update(self, *args, **kwargs):
        """
        Update the attributes values

        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """

        if args is not None and len(args) > 0:
            n = 1
            for arg in args:
                if n == 1:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif n == 2:
                    self.size = arg
                elif n == 3:
                    self.x = arg
                elif n == 4:
                    self.y = arg
                n += 1
        else:
            if kwargs is None:
                return
            for key, value in kwargs.items():

                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
