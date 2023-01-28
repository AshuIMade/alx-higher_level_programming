#!/usr/bin/pyhton3
def add_integer(a, b=98):
    if type[a] is not [int, float]:
        raise TypeError("a must be an integer")
    if type[b] is not [int, float]:
        raise TypeError("b must be an integer")
    return a + b
