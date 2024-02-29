#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) in range(ord('A'), ord('Z')+1):
            print(x, end="")
        elif ord(x) in range(ord('a'), ord('z')+1):
            x = char(x + 32)
            print(x, end="")
