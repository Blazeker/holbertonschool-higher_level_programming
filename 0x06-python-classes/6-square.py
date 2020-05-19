#!/usr/bin/python3
"""Module of Square"""


class Square:
    """ An class called Square """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the data
        And validates if the number is an int
        and > 0
        Size: The size of the square
        Position: The position of the square
        """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """ Gets the value """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the value on size and validate a valid position """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """ Gets the value """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the value on size and validate a valid number"""
        if self.__validate(value):
            self.__size = value

    def __validate(self, size):
        """ Validates if the number is an int and > 0 """
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

    def my_print(self):
        """ Print all the square with # """
        if self.__size == 0:
            print()
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
