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
        """
        returns the JSON string representation of list_dictionaries
        """

        if (list_dictionaries is None):
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        dataJson = "[]"
        if list_objs is not None:
            new = []
            for el in list_objs:
                new.append(el.to_dictionary())

            dataJson = cls.to_json_string(new)

        with open(cls.__name__ + ".json", "w") as file:
            file.write(dataJson)
