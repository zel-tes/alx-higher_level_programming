#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    for i in my_list:
        new_list = list(map(lambda i: number*i, my_list))
    return new_list
