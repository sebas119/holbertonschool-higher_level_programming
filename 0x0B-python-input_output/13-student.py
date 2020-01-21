#!/usr/bin/python3


class Student:

    def __init__(self, first_name, last_name, age):
        """Init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if (isinstance(attrs, list) and
                all(isinstance(el, str) for el in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        for key, val in json.items():
            if (hasattr(self, key)):
                setattr(self, key, val)
