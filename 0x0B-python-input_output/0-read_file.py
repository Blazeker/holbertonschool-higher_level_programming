#!/usr/bin/python3
""" Module of read file """


def read_file(filename=""):
    """ Read a file """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line)
