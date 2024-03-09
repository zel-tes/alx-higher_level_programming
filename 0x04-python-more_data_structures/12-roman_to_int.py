#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    else:
        sum = 0
        roman_num = list(roman_string)
        for i in roman_num:
            if i == 'I':
                sum += 1
            if i == 'V':
                sum += 5
            if i == 'X':
                sum += 10
            if i == 'L':
                sum += 50
            if i == 'C':
                sum += 100
            if i == 'D':
                sum += 500
            if i == 'M':
                sum += 1000
            return sum
