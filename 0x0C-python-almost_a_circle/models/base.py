#!/usr/bin/python3
"""Base module"""
import json
import csv


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
    def create(cls, *mydic, **dictionary):
        """create function"""
        rx = cls(1, 1)
        if len(dictionary) > 0:
            rx.update(**dictionary)
        else:
            rx.update(*mydic)
        return rx

    @classmethod
    def load_from_file(cls):
        """File to instances functions"""
        filename = cls.__name__+".json"
        myList = []
        try:
            with open(filename, "r") as f:
                x = Base.from_json_string(f.read())
                for i in x:
                    myList.append(cls.create(**i))
                return myList
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv function"""
        filename = cls.__name__+".csv"
        if list_objs is None:
            with open(filename, "w") as f:
                f.write("")
        else:
            with open(filename, "w", newline='') as f:
                x = csv.writer(f)
                for i in list_objs:
                    if cls.__name__ == "Rectangle":
                        x.writerow([i.id, i.width, i.height, i.x, i.y])
                    else:
                        x.writerow([i.id, i.size, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """Load from csv function"""
        filename = cls.__name__+".csv"
        myList = []
        try:
            with open(filename, "r") as f:
                x = csv.reader(f)
                for i in x:
                    myList.append(cls.create(*i))
                return myList
        except FileNotFoundError:
            return []
