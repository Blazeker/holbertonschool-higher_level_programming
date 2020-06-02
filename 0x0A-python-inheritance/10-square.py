#!/usr/bin/python3
""" Module for geometry class """


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        string = "[Rectangle] "
        string += str(self.__width) + '/' + str(self.__height)
        return string


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
