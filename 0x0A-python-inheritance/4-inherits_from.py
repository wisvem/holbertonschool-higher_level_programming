#!/usr/bin/python3
"""Is subclass module"""


def inherits_from(obj, a_class):
    """[summary]

    Args:
        obj: object
        a_class: class

    Returns:
        Boolean: true if obj inheritance from class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
