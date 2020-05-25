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
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 2, 1]), 3)
        self.assertEqual(max_integer([1, 3, 3]), 3)
        self.assertEqual(max_integer([4, 4, 3]), 4)
        self.assertEqual(max_integer([1, 2, 10]), 10)
        self.assertEqual(max_integer([0, -2, -1]), 0)
        self.assertEqual(max_integer([-5, -100, -2]), -2)
        self.assertEqual(max_integer([0, -0, 0]), 0)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([0.1]), 0.1)
        self.assertEqual(max_integer([0.1, 0.2, -0.1]), 0.2)
        self.assertEqual(max_integer([-5.9, -5.8, -5.4]), -5.4)

    def test_the_max_emp(self):
        self.assertEqual(max_integer([]), None)

    def test_the_max_neg(self):
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer("Santiago"), max("Santiago"))
        self.assertEqual(max_integer([0, -0, -0.1]), 0)
        self.assertEqual(max_integer([-10000.1, -99.9, -100.1]), -99.9)
        self.assertEqual(max_integer([100.1, 99.9, 100.0]), 100.1)
        self.assertEqual(max_integer([0.0000000000000000000009,
        0.0000000000000000000000000009]), 0.0000000000000000000009)
        self.assertEqual(max_integer([1.0000004, 1.0000008]), 1.0000008)
        self.assertEqual(max_integer("01234567890sS"), max("01234567890sS"))
        self.assertEqual(max_integer([[1, 2, 3], [-100]]), \
            max([[1, 2, 3], [-100]]))
        self.assertEqual(max_integer([float('-inf'), float('inf')]),\
            max([float('-inf'), float('inf')]))

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
