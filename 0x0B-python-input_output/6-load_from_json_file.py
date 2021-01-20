#!/usr/bin/python3
"""object from json module"""
import json


def load_from_json_file(filename):
    """object from json function

    Args:
        filename (json): json file path

    Returns:
        obj: object
    """
    with open(filename, "w") as f:
        return json.loads(f.read())
