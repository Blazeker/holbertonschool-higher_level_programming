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
        if self.__validate(size):
            self.__size = size

    @property
    def size(self):
        """ Gets the value """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the value on size and validate a valid number """
        if self.__validate(value):
            self.__size = value

    def __validate(self, size):
        """ Validates if the number is valid """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False

    def area(self):
        """ Return the area of the square """
        return self.__size ** 2
