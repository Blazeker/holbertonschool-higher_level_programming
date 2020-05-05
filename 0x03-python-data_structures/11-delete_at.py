#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    list_len = len(my_list)
    if list_len == 0:
        return None
    if idx >= 0 and idx < list_len:
        for i in range(list_len):
            if i == idx:
                del my_list[i]
    return(my_list)
