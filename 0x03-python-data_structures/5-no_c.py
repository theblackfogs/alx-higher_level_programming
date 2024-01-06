#!/usr/bin/python3


def no_c(my_string):
    length = len(my_string)

    for i in range(length):
        if my_string[i] == 'c' or my_string[i] == 'C':
            my_string[i] = " "
    return my_string
