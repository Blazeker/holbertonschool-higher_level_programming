#!/usr/bin/python3
""" Module of append write """


def append_write(filename="", text=""):
    """ Append text into a file """
    with open(filename, "a+", encoding='utf-8') as f:
        return (f.write(text))
