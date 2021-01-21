#!/usr/bin/python3
"""Student module"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """init function

        Args:
            first_name ([type]): [description]
            last_name ([type]): [description]
            age ([type]): [description]
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json

        Args:
            attrs ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        obj = {}
        if attrs is not None:
            for i in attrs:
                if hasattr(self, i):
                    obj[i] = getattr(self, i)
            return obj
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """reload arguments

        Args:
            json ([type]): [description]
        """
        for key, value in json.items():
            setattr(self, key, value)
