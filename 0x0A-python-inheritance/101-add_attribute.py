#!/usr/bin/python3
""" Add attribute module class """


def add_attribute(obj, name, value):
    """ Add attribute exercise """

    if hasattr(obj, "__dict__"):
        object.__setattr__(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
