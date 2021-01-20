#!/usr/bin/python3
"""to json module"""
import json


def from_json_string(my_str):
    """json to string function

    Args:
        my_str (json):  json object

    Returns:
        str: string representation
    """
    return json.loads(my_str)
