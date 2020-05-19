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
        if __validateP(value):
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

    def __validateP(self, position):
        """ Validates the 2 positions of the tuple"""
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
            return False
        elif (not isinstance(position, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
            return False
        elif (not isinstance(position[0], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
            return False
        elif(not isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
            return False
        elif (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers") 
            return False
        return True

    def area(self):
        """ Return the area of the square """
        return self.__size ** 2

    def my_print(self):
        """ Print all the square with # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
