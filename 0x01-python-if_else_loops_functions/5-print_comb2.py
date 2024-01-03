#!/usr/bin/python3
w = 2
for i in range(99):
    i = '{:0>{w}}'.format(i, w=w)
    print("{0}, ".format(i), end="")
else:
    print("{}".format("99"))
