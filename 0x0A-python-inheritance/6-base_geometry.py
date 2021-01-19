#!/usr/bin/python3
"""Empty class module"""


class BaseGeometry:
    """Empty basegeometry class"""

    def __init__(self):
        """Init function"""
        pass

    def area(self):
        """area function

        Raises:
            Exception: area not implemented
        """
        raise Exception("area() is not implemented")
