#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super(Square, self).__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """str representation"""
        r = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        r += " - {}".format(self.width)
        return r

    def to_dictionary(self):
        """To dict function"""
        return {"id": self.id, "x": self.x, "size": self.width, "y": self.y}

    def update(self, *args, **kwargs):
        """Update rectangle function"""
        f = []
        f = ["self.id", "self.size", "self.x", "self.y"]
        if len(args) > 0:
            try:
                for i in range(len(args)):
                    exec(f[i] + "= int(args[i])")
            except Exception:
                pass
        else:
            for key, value in kwargs.items():
                x = "self."+key
                exec(x + "= value")
