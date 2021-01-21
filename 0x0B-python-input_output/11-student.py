#!/usr/bin/python3
"""Student module"""
import json

class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """INit function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json function"""
        obj = {}
        if attrs is not None:
            if type(attrs) is list:
                if (all(isinstance(x, str) for x in attrs)):
                    for i in attrs:
                        if hasattr(self, i):
                            obj[i] = getattr(self, i)
                    return obj
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Function to reload att"""
        for key, value in json.items():
            setattr(self, key, value)
