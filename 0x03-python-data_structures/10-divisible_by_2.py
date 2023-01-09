#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res_list = []
    for i in my_list:
        if my_list[i] % 2 == 0:
            res_list.add(True)
        else:
            res_list.add(False)
    return res_list
