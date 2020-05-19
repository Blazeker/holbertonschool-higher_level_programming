#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if self.__validate(size):
            self.__size = size
        if self.__validateP(position):
            self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if __validateP(value):
            self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if self.__validate(value):
            self.__size = value

    def __validate(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False

    def __validateP(self, position):
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
            return False
        return True

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            j = 0
            pos = 0
            for pos in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
