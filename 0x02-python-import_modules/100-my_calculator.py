#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
available_operators = ['+', '-', '*', '/']
if len(sys.argv) != 4 :
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
else:
    if sys.argv[2] in available_operators:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == '+':
            print("{} {} {} = {}".format(a, '+', b, add(a, b)))
        elif sys.argv[2] == '-':
            print("{} {} {} = {}".format(a, '-', b, sub(a, b)))
        elif sys.argv[2] == '*':
            print("{} {} {} = {}".format(a, '*', b, mul(a, b)))
        else:
            print("{} {} {} = {}".format(a, '/', b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

if "__name__" == "__main__":
    main()


