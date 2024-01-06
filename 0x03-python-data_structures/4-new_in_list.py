#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    length = len(my_list) - 1
    copy = my_list[:]

    if idx < 0 or idx > length:
        return copy
    else:
        copy[idx] = element
        return copy
