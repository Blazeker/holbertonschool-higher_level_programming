#!/usr/bin/python3
""" Print a string with certain cases """


def text_indentation(text):
    """ Print a string with special cases like '.', '?', ':'
        when encounter that cases print double \n
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for x in ".:?":
        text = (x + "\n\n").join([w.strip(" ") for w in text.split(x)])
    print(text, end="")
