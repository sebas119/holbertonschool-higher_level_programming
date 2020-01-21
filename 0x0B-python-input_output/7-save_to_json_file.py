#!/usr/bin/python3

"""object JSON to a file module"""

import json


def save_to_json_file(my_obj, filename):
    """Save object representation of JSON to a file"""

    with open(filename, mode='w', encoding='UTF-8') as myfile:

        json.dump(my_obj, myfile)
