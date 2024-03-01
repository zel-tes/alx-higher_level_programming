#!/usr/bin/python3
def remove_char_at(str, n):
    l = len(str)
    new_str = ""
    for i in range(l):
        if i == n:
            continue
        else:
            new_str += str[i]
    return new_str
