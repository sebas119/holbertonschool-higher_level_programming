#!/usr/bin/python3
"""Json to string module"""

import json


def to_json_string(my_obj):
    """Function that return the JSON representation of
    an object"""

    return json.dumps(my_obj)
