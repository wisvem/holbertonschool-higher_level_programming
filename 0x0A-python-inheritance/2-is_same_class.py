#!/usr/bin/python3
""" is same class module """


def is_same_class(obj, a_class):
    """[summary]

    Args:
        obj (obj): the object
        a_class (class): the class

    Returns:
        Boolean: if obj is an instance of class
    """
    return type(obj) is a_class
