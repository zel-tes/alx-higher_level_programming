#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
   sorted_list_a = sorted(a_dictionary.items(), key = lambda x: x[0])
   a_dictionary = dict(sorted_list_a)
   for key, value in a_dictionary.items():
       print(key, value, sep=": ")
