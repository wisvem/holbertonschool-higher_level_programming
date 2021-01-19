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

    def integer_validator(self, name, value):
        """[summary]

        Args:
            name ([type]): [description]
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
