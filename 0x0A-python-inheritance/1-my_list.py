#!/usr/bin/python3
""" Module for my list class """


class MyList(list):
    """ Print sorted list inhertied """

    def print_sorted(self):
        """ print list sorted """
        print(sorted(self))
