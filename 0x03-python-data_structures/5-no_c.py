#!/usr/bin/python3
def no_c(my_string):
    copy_str = [ch for ch in my_string if ch != 'c' or ch != 'C']
    return copy_str
