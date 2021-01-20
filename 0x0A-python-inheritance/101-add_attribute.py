#!/usr/bin/python3
"""Add atribute module"""


def add_attribute(object, att, value):
    """Add attribute function"""
    if hasattr(object, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(object, att, value)
