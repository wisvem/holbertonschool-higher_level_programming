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
        self.__widhth = width
        self.__height = height
