#!/usr/bin/python3

def uppercase(str):
    length = len(str)

    for i in range(0, length):
        a_value = ord(str[i])
        if a_value > 96 and a_value < 123:
            a_value -= 32
        print("{}".format(chr(a_value)), end="")
    print()
