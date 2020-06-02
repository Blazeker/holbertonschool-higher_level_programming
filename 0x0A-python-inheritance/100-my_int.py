#!/usr/bin/python3
""" My int module class """


class MyInt(int):
    """ My int exercise """

    def __eq__(self, other):
        return (int(self) != other)

    def __ne__(self, other):
        return (int(self) == other)
