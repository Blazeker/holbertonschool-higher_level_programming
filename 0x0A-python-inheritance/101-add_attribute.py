#!/usr/bin/python3
""" Add attribute module class """


def add_attribute(obj, name, value):
    """ Add attribute exercise """

    type_z = (str, int, complex, bool, float, list, tuple, dict,
              set, frozenset, type, object)
    for type_s in type_z:
        if type(obj) is type_s:
            raise TypeError("can't add new attribute")

    object.__setattr__(obj, name, value)
