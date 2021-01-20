#!/usr/bin/python3
"""to json module"""
import json


def to_json_string(my_obj):
    """to json function

    Args:
        my_obj (obj): object

    Returns:
        json: json object
    """
    return json.dumps(my_obj)
