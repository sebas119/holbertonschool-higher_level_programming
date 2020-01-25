#!/usr/bin/python3

"""Defines a class Base."""

import json
import csv


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

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """

        list_instances = []

        try:
            with open(cls.__name__ + ".json", 'r') as file:
                data = cls.from_json_string(file.read())
        except FileNotFoundError:
            return list_instances

        for el in data:
            list_instances.append(cls.create(**el))

        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes the list_objs to a file in this format:
        * Rectangle: <id>,<width>,<height>,<x>,<y>
        * Square: <id>,<size>,<x>,<y>
        """

        filename = cls.__name__
        for el in list_objs:
            print(cls.__name__ == "Rectangle")
            print(cls.__name__ == "Square")
            for key, value in el.to_dictionary().items():
                pass

    @classmethod
    def load_from_file_csv(cls):
        """

        """

        filename = cls.__name__
