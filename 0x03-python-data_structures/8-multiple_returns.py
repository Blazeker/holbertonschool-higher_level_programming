#!/usr/bin/python3
def multiple_returns(sentence):
    len_s = len(sentence)
    if len_s == 0:
        new_tuple = None
    else:
        new_tuple = sentence[0]
    return((len_s, new_tuple))
