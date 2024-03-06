#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = list.reverse(my_list)
    for i in my_list:
        print("{:d}".format(i))
