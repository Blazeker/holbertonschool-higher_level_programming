#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if self.__validate(size):
            self.__size = size

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

    def area(self):
        return self.__size ** 2

    def my_print(self):
            for i in range(0, self.__size):
                j = 0
                for j in range(0, self.__size):
                    print("#", end='')
                print()
