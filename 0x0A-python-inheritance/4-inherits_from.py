#!/usr/bin/python3
""" module for the inherit class """


def inherits_from(obj, a_class):
    """ returns the inherit types """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
