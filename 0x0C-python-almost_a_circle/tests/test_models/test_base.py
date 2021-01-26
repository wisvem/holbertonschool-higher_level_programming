#!/usr/bin/python3
"""Unit test for base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit test for base"""
    print("######Initialization Base tests######")
    # Initialization test

    def test01(self):
        """Set auto id 1"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test02(self):
        """Set auto id 2"""
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test03(self):
        """Set manual id"""
        b3 = Base(15)
        self.assertEqual(b3.id, 15)

    def test04(self):
        """Chek auto id after manual id"""
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test05(self):
        """Check multiple arguments"""
        with self.assertRaises(TypeError):
            b5 = Base(1, 2, 3)

    def test06(self):
        """Check id None argument"""
        b6 = Base(None)
        self.assertEqual(b6.id, 4)

    def test07(self):
        """Set string as id"""
        b7 = Base("string")
        self.assertEqual(b7.id, "string")

    # Attributes tests
    def test08(self):
        """Check if class attribute exist"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test09(self):
        """Check last id given"""
        self.assertEqual(Base._Base__nb_objects, 4)

    def test10(self):
        """Acces private class attribute"""
        b8 = Base()
        self.assertEqual(b8._Base__nb_objects, 5)

    def test11(self):
        """Test Attribute error"""
        b9 = Base()
        with self.assertRaises(AttributeError):
            b9.__nb_objects
       