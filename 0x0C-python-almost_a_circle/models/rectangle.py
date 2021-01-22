#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor class"""
        self.width(width)
        self.height(height)
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value): 
        print(type(value))
        self.integer_validator("height", value)
        self.height = value

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.x = value

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.y = value

    def integer_validator(self, name, value):
        """Integer validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and name in ("width", "height"):
            raise ValueError("{} must be > 0".format(name))
        if value < 0 and name in ("x", "y"):
            raise ValueError("{} must be >= 0".format(name))
