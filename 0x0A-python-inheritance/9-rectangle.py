#!/usr/bin/python3
"""Empty class module"""
BG = __import__('7-base_geometry').BaseGeometry


class Rectangle(BG):
    """Rectangle class"""

    def __init__(self, width, height):
        """[summary]

        Args:
            width ([type]): [description]
            height ([type]): [description]
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area method

        Returns:
            int: rectangle area
        """
        return self.__height * self.__width

    def __str__(self):
        """overloading str method

        Returns:
            str: rectangle data
        """
        sr = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return sr
