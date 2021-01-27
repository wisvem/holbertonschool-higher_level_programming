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
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        filename = cls.__name__+".json"
        myList = []
        if list_objs is None:
            with open(filename, "w") as f:
                f.write("[]")
        else:
            for i in list_objs:
                myList.append(i.to_dictionary())
            myStr = Base.to_json_string(myList)
            with open(filename, "w") as f:
                f.write(myStr)

    def from_json_string(json_string):
        """from json to string function"""
        return json.loads(json_string)

    # @classmethod
    # def create(cls, *mydic, **dictionary):
    #     """create function"""
    #     rx = cls(1, 1)
    #     if len(dictionary) > 0:
    #         rx.update(**dictionary)
    #     else:
    #         rx.update(*mydic)
    #     return rx

    @classmethod
    def create(cls, **dictionary):
        """create function v2"""
        rx = cls(1, 1)
        rx.update(**dictionary)
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
        el = []
        if list_objs is None or bool(list_objs) is False:
            with open(filename, "w") as f:
                x = csv.writer(f)
                x.writerows(el)
        else:
            with open(filename, "w", newline='') as f:
                x = csv.writer(f)
                if cls.__name__ == "Rectangle":
                    x.writerow(["id", "width", "height", "x", "y"])
                    command = 'x.writerow([i.id, i.width, i.height, i.x, i.y])'
                else:
                    x.writerow(["id", "size", "x", "y"])
                    command = 'x.writerow([i.id, i.size, i.x, i.y])'
                for i in list_objs:
                    exec(command)

    @classmethod
    def load_from_file_csv(cls):
        """Load from csv function"""
        filename = cls.__name__+".csv"
        myList = []
        ln = 0
        if cls.__name__ is "Rectangle":
            keys = ["id", "width", "height", "x", "y"]
        else:
            keys = ["id", "size", "x", "y"]
        try:
            with open(filename, "r") as f:
                x = csv.reader(f)
                for i in x:
                    if ln > 0:
                        myDict = dict(zip(keys, map(int, i)))
                        myList.append(cls.create(**myDict))
                    ln += 1
                return myList
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw function"""
        import turtle
        import random
        turtle.bgcolor("black")
        t = turtle.Turtle()
        t.shape("turtle")
        t.shapesize(1)
        t.pensize(3)
        t.speed(3)
        for i in list_squares:
            R = random.random()
            B = random.random()
            G = random.random()
            t.color(R, G, B)
            t.up()
            t.goto(i.x, i.y)
            t.down()
            for x in range(4):
                t.forward(i.size)
                t.left(90)
        for i in list_rectangles:
            R = random.random()
            B = random.random()
            G = random.random()
            t.color(R, G, B)
            t.up()
            t.goto(i.x, i.y)
            t.down()
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
        t.hideturtle()
        turtle.done()
