#!/usr/bin/python3
"""find a peak in integers list"""


def find_peak(list_of_integers):
    if list_of_integers is None or list_of_integers == []:
        return None
    hi = list_of_integers[0]
    for i in range(len(list_of_integers)):
        if hi <= list_of_integers[i]:
            hi = list_of_integers[i]
    return hi
