#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return ([el if el != search else replace for el in my_list])
