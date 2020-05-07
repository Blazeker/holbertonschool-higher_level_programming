#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    res = 0.0
    s_list = list(weight[0] * weight[1] for t in my_list)
    w_list = list(weight[1] for weight in my_list)
    res = sum(s_list) / sum(w_list)
    return res
