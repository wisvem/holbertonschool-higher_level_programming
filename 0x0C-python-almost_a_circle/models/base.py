#!/usr/bin/python3
"""Base module"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor

        Args:
            id (int, optional): an int. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """json to string dict"""
        if len(list_dictionaries) is 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        filename = cls.__name__+".json"
        if list_objs is not None:
            return
            with open(filename, "w") as f:
                f.write(Base.to_json_string(list_objs))
