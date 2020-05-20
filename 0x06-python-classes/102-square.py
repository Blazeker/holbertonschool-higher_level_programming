#!/usr/bin/python3
"""Module of Square"""


class Square:
    """ An class called Square """

    def __init__(self, size=0):
        """
        Initialize the data
        And validates if the number is an int
        and > 0
        Size: The size of the square
        """
        self.size = size

    @property
    def size(self):
        """ Gets the value """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the value on size and validate a valid number """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return the area of the square """
        return self.__size ** 2

    def __eq__(self, osquare):
        """The == comparison"""
        return self.area() == osquare.area()

    def __ne__(self, osquare):
        """The != comparison"""
        return self.area() != osquare.area()

    def __lt__(self, osquare):
        """The < comparison"""
        return self.area() < osquare.area()

    def __le__(self, osquare):
        """The <= comparison"""
        return self.area() <= osquare.area()

    def __gt__(self, osquare):
        """The > comparison"""
        return self.area() > osquare.area()

    def __ge__(self, osquare):
        """The >= comparison"""
        return self.area() >= osquare.area()
