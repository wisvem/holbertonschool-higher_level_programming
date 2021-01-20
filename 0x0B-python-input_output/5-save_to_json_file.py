#!/usr/bin/python3
"""string to json file module """
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj ([type]): [description]
        filename ([type]): [description]
    """
    with open(filename, "a") as f:
        f.write(json.dumps(my_obj))
