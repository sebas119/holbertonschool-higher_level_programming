#!/usr/bin/python3

"""Defines a subclass inherited from list."""


class MyList(list):
    """Class MyList"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
