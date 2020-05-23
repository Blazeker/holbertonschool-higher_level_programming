#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Testing max integer problem
    """

    def test_the_max(self):
        T_list = [10, 20, 30, 40, 50]
        self.assertEqual(max_integer(T_list), 50)

    def test_the_max_emp(self):
        self.assertEqual(max_integer([]), None)

    def test_the_max_neg(self):
        T_list = [10, 20, 30, -5, 40, -10, -20]
        self.assertEqual(max_integer(T_list), 40)

    def test_the_max_one(self):
        T_list = [1]
        self.assertEqual(max_integer(T_list), 1)

    def test_the_max_neg2(self):
        T_list = [-10, -20, -30, -5, -40, -10, -20]
        self.assertEqual(max_integer(T_list), -5)

    def test_the_max_repeat(self):
        T_list = [1, 1, 1, 1, 1]
        self.assertEqual(max_integer(T_list), 1)

    def test_the_max_one(self):
        T_list = [5]
        self.assertEqual(max_integer(T_list), 5)

    def test_string(self):
        string = "Santiago"
        self.assertEqual(max_integer(string), 't')

    def test_list_of_strings(self):
        strings = ["Hola", "Crack", "s", "ssss"]
        self.assertEqual(max_integer(strings), "ssss")

    def test_errors(self):
        with self.assertRaises(TypeError):
            max_integer(False)
        with self.assertRaises(TypeError):
            max_integer(-5555555)
        with self.assertRaises(TypeError):
            max_integer(5555555)