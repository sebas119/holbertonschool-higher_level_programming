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
        except IOError:
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

        with open(cls.__name__ + ".csv", "w") as mycsv:
            if list_objs is None or list_objs == []:
                mycsv.write("[]")
            else:
                list_data = []
                for el in list_objs:
                    if cls.__name__ == "Rectangle":
                        data = ["id", "width", "height", "x", "y"]
                    elif cls.__name__ == "Square":
                        data = ["id", "size", "x", "y"]
                    for key, value in el.to_dictionary().items():
                        if len(data) == 5:
                            if key == "id":
                                data[0] = str(value)
                            elif key == "width":
                                data[1] = str(value)
                            elif key == "height":
                                data[2] = str(value)
                            elif key == "x":
                                data[3] = str(value)
                            elif key == "y":
                                data[4] = str(value)
                        elif len(data) == 4:
                            if key == "id":
                                data[0] = str(value)
                            elif key == "size":
                                data[1] = str(value)
                            elif key == "x":
                                data[2] = str(value)
                            elif key == "y":
                                data[3] = str(value)
                    data = ",".join([str(el) for el in data])
                    list_data.append(data)
                for el in list_data:
                    mycsv.write(el)
                    mycsv.write("\n")

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads the list_objs from a file in this format:
        * Rectangle: <id>,<width>,<height>,<x>,<y>
        * Square: <id>,<size>,<x>,<y>
        """
        try:
            with open(cls.__name__ + ".csv", "r") as mycsv:
                raw_data = mycsv.readlines()
                list_data = []
                for el in raw_data:
                    new = el.replace('\n', '')
                    list_data.append(new)
                list_instances = []
                for el in list_data:
                    clean_list = el.split(',')
                    if cls.__name__ == "Rectangle":
                        data = {"id": 0, "width": 0,
                                "height": 0, "x": 0, "y": 0}
                    elif cls.__name__ == "Square":
                        data = {"id": 0, "size": 0, "x": 0, "y": 0}
                    if len(clean_list) == 5:
                        data["id"] = int(clean_list[0])
                        data["width"] = int(clean_list[1])
                        data["height"] = int(clean_list[2])
                        data["x"] = int(clean_list[3])
                        data["y"] = int(clean_list[4])
                    elif len(clean_list) == 4:
                        data["id"] = int(clean_list[0])
                        data["size"] = int(clean_list[1])
                        data["x"] = int(clean_list[2])
                        data["y"] = int(clean_list[3])
                    list_instances.append(cls.create(**data))

                return list_instances
        except IOError:
            return []
