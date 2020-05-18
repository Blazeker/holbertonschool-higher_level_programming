#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_L = []
    cont = 0
    for i in my_list:
        if i not in new_L:
            cont += i
            new_L.append(i)
    return(cont)
