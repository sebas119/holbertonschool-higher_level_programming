#!/usr/bin/python3

"""Defines a class Base."""

import json


class Base:
    """Represent a Base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):

        if (list_dictionaries is None):
            return "[]"

        return json.dumps(list_dictionaries)
