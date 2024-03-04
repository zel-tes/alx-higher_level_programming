#!/usr/bin/python3
toggle = True
for x in range(122, 97, -1):
    if toggle:
        print("{0}{1}".format(chr(x), chr(x-33)), end="")
    toggle = not toggle
