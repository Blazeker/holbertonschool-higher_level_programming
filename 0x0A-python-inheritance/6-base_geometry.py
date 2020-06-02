#!/usr/bin/python3
""" Module for geometry class """


class BaseGeometry():
    """ Geometry class with empty area """

    def area(self):
        raise Exception("area() is not implemented")
