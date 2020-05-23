#!/usr/bin/python3
""" Print a square with # """


def print_square(size):
    """ Print the size of a square with the char '#' """
    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")
    if size < 0:
        if type(size) is float:
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
    size = int(size)

    for i in range(0, size):
        j = 0
        for j in range(0, size):
            print("#", end="")
        print()
