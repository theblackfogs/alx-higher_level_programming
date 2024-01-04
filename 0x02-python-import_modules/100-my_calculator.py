#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    length = len(argv)
    temp = 0
    if length == 4:
        if argv[2] == '+':
            temp = add(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], temp))
        elif argv[2] == '-':
            temp = sub(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], temp))
        elif argv[2] == '*':
            temp = mul(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], temp))
        elif argv[2] == '/':
            temp = div(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], temp))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
