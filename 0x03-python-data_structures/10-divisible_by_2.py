#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mult_of_2 = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            mult_of_2.append(True)
        else:
            mult_of_2.append(False)
    return mult_of_2
