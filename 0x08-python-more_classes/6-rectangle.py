#!/usr/bin/python3
"""Rectangle module"""


class Rectangle():
    """Rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instance definition

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): heigth of rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Method to get te area

        Returns:
            int: rectangle area
        """
        return self.__height*self.__width

    def perimeter(self):
        """Method to get perimeter

        Returns:
            int: perimeter
        """
        if self.area() == 0:
            return 0
        return 2*(self.__height+self.__width)

    def __str__(self):
        """str representation

        Returns:
            str: a string
        """
        if self.area() == 0:
            return ""
        pt = ""
        for i in range(self.height):
            for j in range(self.width):
                pt = pt + "#"
            if i < self.height - 1:
                pt = pt + "\n"
        return pt

    def __repr__(self):
        """repr overload

        Returns:
            repr : non ambiguos representation
        """
        r = "{self.__class__.__name__}({self.width}, {self.height})".format(
            self=self)
        return r

    def __del__(self):
        """Overloading del method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
