#!/usr/bin/python3
""" Print a string with certain cases """


def text_indentation(text):
    """ Print a string with special cases like '.', '?', ':'
        when encounter that cases print double \n
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    special = ['.', '?', ':']
    aux_s = ""
    for chara in text:
        aux_s += chara
        if chara in special:
            aux_s += "\n\n"
    print(aux_s, end="")
