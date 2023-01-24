#!/usr/bin/python3


""""Class Square"""


class Square:

    def __init__(self, size = 0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size value must be >=0")
        self.__size = size
