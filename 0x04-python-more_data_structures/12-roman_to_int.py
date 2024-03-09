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
            elif i == 'V':
                sum += 5
            elif i == 'X':
                sum += 10
            elif i == 'L':
                sum += 50
            elif i == 'C':
                sum += 100
            elif i == 'D':
                sum += 500
            elif i == 'M':
                sum += 1000
        return sum
