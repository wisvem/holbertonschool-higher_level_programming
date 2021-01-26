#!/usr/bin/python3
"""Unittest for base.py file
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class Test_rectangle(unittest.TestCase):
    """Defines a class to evaluate diferent test cases for base.py file"""

    def test_instance_class(self):
        """Checks for a instance of the class"""
        r1 = Rectangle(10, 2)
        self.assertIsInstance(r1, Rectangle)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertTrue(id(Rectangle) != id(Base))
        self.assertTrue(type(Rectangle) == type(Base))
        r2 = Rectangle(2, 5)
        self.assertTrue(type(r1) == type(r2))
        self.assertFalse(id(r1) == id(r2))

    def test_init_attributes(self):
        """Checks when id is none"""
        r1 = Rectangle(10, 60)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 60)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(20, 40)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 20)
        self.assertEqual(r2.height, 40)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(10, 2, 4, 5)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 4)
        self.assertEqual(r3.y, 5)

        r4 = Rectangle(10, 2, 6)
        self.assertEqual(r4.id, 4)
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 6)
        self.assertEqual(r4.y, 0)

        r5 = Rectangle(10, 2, 4, 5, 50)
        self.assertEqual(r5.id, 50)
        self.assertEqual(r5.width, 10)
        self.assertEqual(r5.height, 2)
        self.assertEqual(r5.x, 4)
        self.assertEqual(r5.y, 5)

        r6 = Rectangle(10, 2, 4, 5, 180)
        r6.id = 50
        self.assertEqual(r6.id, 50)
        r6.width = 100
        self.assertEqual(r6.width, 100)
        r6.height = 200
        self.assertEqual(r6.height, 200)
        r6.x = 40
        self.assertEqual(r6.x, 40)
        r6.y = 50
        self.assertEqual(r6.y, 50)

    def test_raise_errors(self):
        """Check for raises errors
        """
        print("--->Check for important raises errors")
        with self.assertRaises(TypeError):
            r1 = Rectangle()
        with self.assertRaises(NameError):
            r1 = Rectangle_shape()
        with self.assertRaises(AttributeError):
            r1 = Rectangle(10, 80)
            r1.to_json()
        with self.assertRaises(TypeError):
            r2 = Rectangle(10)
        with self.assertRaises(ValueError):
            r3 = Rectangle(10, -4)
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, "4")
        with self.assertRaises(TypeError):
            r5 = Rectangle("10", 4)
        with self.assertRaises(TypeError):
            r6 = Rectangle(10, 4, "9")
        with self.assertRaises(TypeError):
            r7 = Rectangle(10, 4, 9, "20")
        with self.assertRaises(ValueError):
            r8 = Rectangle(10, 4, -5, 7)
        with self.assertRaises(ValueError):
            r9 = Rectangle(10, 4, 5, -10)
        with self.assertRaises(ValueError):
            r1.x = -4
        with self.assertRaises(ValueError):
            r1.width = -10
        with self.assertRaises(TypeError):
            r1.width = "10"

    def test_area(self):
        """Check area method of rectangle objects
        """
        print("---> Checks area method")
        r1 = Rectangle(3, 2)
        area = r1.area()
        self.assertEqual(area, 6)

        r2 = Rectangle(3, 2)
        area = Rectangle.area(r2)
        self.assertEqual(area, 6)

        r3 = Rectangle(30, 20, 4, 5, 10)
        area = r3.area()
        self.assertEqual(area, 600)

        r4 = Rectangle(5, 5, 4)
        area = r4.area()
        self.assertEqual(area, 25)

    def test_display(self):
        output_1 = "#\n"
        r1 = Rectangle(1, 1)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            r1.display()
            self.assertEqual(mock_out.getvalue(), output_1)

        output_2 = "#####\n#####\n"
        r2 = Rectangle(5, 2)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            r2.display()
            self.assertEqual(mock_out.getvalue(), output_2)

        output_3 = "\n\n##\n##\n"
        r3 = Rectangle(2, 2, 0, 2)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            r3.display()
            self.assertEqual(mock_out.getvalue(), output_3)

        output_4 = "  ##\n  ##\n"
        r4 = Rectangle(2, 2, 2, 0)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            r4.display()
            self.assertEqual(mock_out.getvalue(), output_4)

        output_5 = "\n\n  ##\n  ##\n"
        r5 = Rectangle(2, 2, 2, 2)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            r5.display()
            self.assertEqual(mock_out.getvalue(), output_5)

    def tearDown(self):
        """Tear down test method
        """
        print("Tear down - Reset nb_object attribute to zero")
        Base._Base__nb_objects = 0
