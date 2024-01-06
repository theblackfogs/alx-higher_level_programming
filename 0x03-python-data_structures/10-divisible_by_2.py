#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    length = len(my_list)
    new = []

    for i in range(length):
        if my_list[i] % 2 == 0:
            new.insert(i, True)
        else:
            new.insert(i, False)

    return new
