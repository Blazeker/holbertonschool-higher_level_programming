#!/usr/bin/python3
""" Module that read the lines """


def read_lines(filename="", nb_lines=0):
    """ Read the n lines """
    cont = 0
    with open(filename, encoding='utf-8') as f:
        if cont < nb_lines or nb_lines <= 0:
            for line in f:
                print(line, end="")
                cont += 1
