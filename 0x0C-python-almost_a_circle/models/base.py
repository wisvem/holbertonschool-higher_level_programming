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
        myList = []
        if list_objs is None:
            with open(filename, "w") as f:
                f.write(myList)
        else:
            for i in list_objs:
                myList.append(i.to_dictionary())
            myStr = Base.to_json_string(myList)
            with open(filename, "w") as f:
                f.write(myStr)

    def from_json_string(json_string):
        """from json to string function"""
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create function"""
        rx = cls(1, 1)
        rx.update(**dictionary)
        return rx
