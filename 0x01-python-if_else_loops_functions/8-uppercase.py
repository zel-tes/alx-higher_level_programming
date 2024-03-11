#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) not in range(97, 123):
            print("{}".format(x), end="")
        elif ord(x) in range(97, 123):
            x = ord(x) - 32
            print("{}".format(chr(x)), end="")
    print()
