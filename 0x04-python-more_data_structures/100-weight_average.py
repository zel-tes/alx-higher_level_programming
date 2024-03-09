#!/usr/bin/python3
def weight_average(my_list=[]):
    total_score = 0
    total_weight = 0
    if my_list == []:
        return 0
    for score in my_list:
        total_score += score[0] * score[1]
        total_weight += score[1]
    return total_score / total_weight
