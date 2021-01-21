#!/usr/bin/python3
"""class to json module"""


def class_to_json(obj):
    """class to json module

    Args:
        obj ([type]): [description]

    Returns:
        [type]: [description]
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__
