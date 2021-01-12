#!/usr/bin/python3
"""Rectangle module"""


class Rectangle():
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Instance definition

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): heigth of rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """get function

        Returns:
            int: width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """height getter

        Returns:
            int: heigth
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter

        Args:
            value (int): argument

        Raises:
            TypeError: if not integer
            ValueError: if value less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """setter

        Args:
            value (int): argument

        Raises:
            TypeError: if not integer
            ValueError: if value less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
