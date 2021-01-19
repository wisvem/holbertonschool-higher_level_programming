#!/usr/bin/python3
"""Dict module"""


def lookup(obj):
    """list of available attributes and methods of an object

    Args:
        obj (obj): object

    Returns:
        list: list of attributes
    """
    return list(dir(obj))
