#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    list_1 = list(a_dictionary.keys())
    list_2 = sorted(a_dictionary.values())
    list_3 = list(a_dictionary.values())
    best = list_2[-1]
    for i in range(len(list_3)):
        if list_3[i] == best:
            best = list_1[i]
    return best
