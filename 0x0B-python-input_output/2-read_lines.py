#!/usr/bin/python3
""" Module that read the lines """


def read_lines(filename="", nb_lines=0):
    """ Read the n lines """
    cont = 0
    with open(filename, encoding='utf-8') as f:
        if (nb_lines <= 0):
                print(f.read(), end="")
        else:
            while (cont < nb_lines):
                print(f.read(), end="")
                cont += 1
