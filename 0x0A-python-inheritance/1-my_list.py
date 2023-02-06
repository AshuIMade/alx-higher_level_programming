#!/usr/bin/python3
"""A class that inherits from List class"""


class MyList(list):
    """A class that inherits from a list class"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
