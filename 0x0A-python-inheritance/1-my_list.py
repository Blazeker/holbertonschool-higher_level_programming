#!/usr/bin/python3
""" Module for my list class """


class MyList(list):
    """ Print sorted list """
    def print_sorted(self):
        print(sorted(self)
