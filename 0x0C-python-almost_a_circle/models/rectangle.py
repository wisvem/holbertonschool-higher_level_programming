#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        """Integer validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and name in ("width", "height"):
            raise ValueError("{} must be > 0".format(name))
        if value < 0 and name in ("x", "y"):
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Area function"""
        return self.__height * self.__width

    def display(self):
        """Display function"""
        print("\n"*self.__y, end="")
        for i in range(self.__height):
            print(" "*self.__x, "#"*self.__width, sep="")

    def __str__(self):
        """str representation"""
        r = "[Rectangle] ({}) {}/{}".format(self.id, self.__x, self.__y)
        r += " - {}/{}".format(self.__width, self.__height)
        return r

    def update(self, *args, **kwargs):
        """Update rectangle function"""
        f = []
        if type(self) is Rectangle:
            f = ["self.id", "self.width", "self.height",
                 "self.x", "self.y"]
        else:
            f = ["self.id", "self.size",
                 "self.x", "self.y"]

        if len(args) > 0:
            try:
                for i in range(len(args)):
                    exec(f[i] + "= int(args[i])")
            except Exception:
                pass
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                x = "self."+key
                exec(x + "= value")

    def to_dictionary(self):
        """To dict function"""
        return {"x": self.x, "y": self.y, "id": self.id, "height": self.height,
                "width": self.width}
