#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit test for module to find the max integer in a list
    """

    def test01(self):
        """"Test good arguments 1"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test02(self):
        """"Test good arguments 2"""
        self.assertEqual(max_integer([1, 12, 3, 4]), 12)

    def test03(self):
        """"Test good arguments 3"""
        self.assertEqual(max_integer([-10, -20, -3, -45]), -3)

    def test04(self):
        """Test no arguments"""
        self.assertEqual(max_integer(), None)

    def test05(self):
        """max value duplicated"""
        self.assertEqual(max_integer([-10, -20, -3, -3]), -3)

    def test06(self):
        """empty list"""
        self.assertEqual(max_integer([]), None)

    def test07(self):
        """one number"""
        self.assertEqual(max_integer([-3]), -3)

    def test08(self):
        """string as argument"""
        self.assertEqual(max_integer("abcwdefg"), "w")

    def test09(self):
        """tuple as argument"""
        self.assertEqual(max_integer((-10, -20, -3, -3)), -3)

    def test10(self):
        """integer directly to raises error"""
        with self.assertRaises(TypeError):
            max_integer(-10, -20, -3, -3)

    def test11(self):
        """list of strings"""
        self.assertEqual(max_integer(
            ["hola", "mundo", "cruel", "god"]), "mundo")

    def test12(self):
        """to the infinity and beyond"""
        self.assertEqual(max_integer(
            [float('inf'), float('-inf')]), float('inf'))

    def test13(self):
        """scientific notation"""
        self.assertEqual(max_integer([1000e+100, -1000e+100]), 1000e+100)

    def test14(self):
        """list of strings"""
        with self.assertRaises(TypeError):
            max_integer(["hola", "12345", "cruel", 980336])

    def test15(self):
        """floats a integers mixed"""
        self.assertEqual(max_integer([-3.7, -3.9, -4]), -3.7)

    def test16(self):
        """floats"""
        self.assertEqual(max_integer([-3.7, -3.9, 5.5]), 5.5)

    def test17(self):
        """big negative float"""
        self.assertEqual(max_integer([-3.141618, -3.9, -5.5]), -3.141618)

    def test18(self):
        """Value error"""
        with self.assertRaises(ValueError):
            max_integer([-3.7, int("dog"), 5.5])

    def test16(self):
        """Inception"""
        self.assertEqual(max_integer([-3.7, -3.9, max_integer([2, 10])]), 10)
