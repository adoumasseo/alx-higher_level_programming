#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxi = my_list[0]
    for ele in my_list:
        if ele > maxi:
            maxi = ele
    return maxi
