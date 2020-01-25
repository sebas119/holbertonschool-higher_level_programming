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
        Returns the JSON string representation of list_dictionaries
        """

        if (list_dictionaries is None):
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        dataJson = "[]"
        if list_objs is not None:
            new = []
            for el in list_objs:
                new.append(el.to_dictionary())

            dataJson = cls.to_json_string(new)

        with open(cls.__name__ + ".json", "w") as file:
            file.write(dataJson)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """

        if json_string is None or json_string is "[]":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """

        r = cls(1, 1, 1, 1)
        r.update(**dictionary)
        return r
