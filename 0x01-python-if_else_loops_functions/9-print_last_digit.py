#!/usr/bin/python3

last = 0


def print_last_digit(number):

    if number < 0:
        last = ((number * -1) % 10)
    else:
        last = number % 10
    print(f"{last}", end="")
    return last
