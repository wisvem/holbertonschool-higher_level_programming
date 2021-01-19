#!/usr/bin/python3
""" is same class module """


def is_kind_of_class(obj, a_class):
    """[summary]

    Args:
        obj (obj): the object
        a_class (class): the class

    Returns:
        Boolean: if obj is an instance of class
    """
    return isinstance(obj, a_class)
