#!/usr/bin/python3
"""Student module"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """INit function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to json function"""
        return self.__dict__
