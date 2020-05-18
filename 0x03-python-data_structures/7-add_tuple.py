#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tu_len = len(tuple_a)
    tub_len = len(tuple_b)
    new_tup = ()
    for i in range(2):
        if i >= tu_len:
            val_a = 0
        else:
            val_a = tuple_a[i]
        if i >= tub_len:
            val_b = 0
        else:
            val_b = tuple_b[i]

        if (i == 0):
            new_tup = (val_a + val_b)
        else:
            new_tup = (new_tup, val_a + val_b)
    return (new_tup)
