#!/usr/bin/python3
def copy_list(l):
    if type(l) is not list:
        return None
    return l[:]
