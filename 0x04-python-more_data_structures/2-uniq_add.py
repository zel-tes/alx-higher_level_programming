#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    new_list = list(set(my_list))
    for i in new_list:
        sum += i
    return sum
