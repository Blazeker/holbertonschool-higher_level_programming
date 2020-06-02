#!/usr/bin/python3
""" module for the kind class """


def is_kind_of_class(obj, a_class):
    """ returns the comparison between obj and a_class """
    return (isinstance(obj, a_class) or issubclass(type(obj), a_class))
