#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res_list = []
    for i in len(my_list) - 1 :
        if my_list[i] % 2 == 0:
            res_list.insert(True)
        else:
            res_list.insert(False)
    return res_list
