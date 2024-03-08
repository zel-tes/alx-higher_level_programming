#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    elif roman_string is not str:
        return 0
    else:
        sum = 0
        roman_num = []
        roman_num.append(roman_string.split())
        for i in range(len(roman_num)):
            if roman_num[i] == 'I':
                sum += 1
            if roman_num[i] == 'V':
                sum += 5
            if roman_num[i] == 'X':
                sum += 10
            if roman_num[i] == 'L':
                sum += 50
            if roman_num[i] == 'C':
                sum += 100
            if roman_num[i] == 'D':
                sum += 500
            if roman_num[i] == 'M':
                sum += 1000
                return sum
