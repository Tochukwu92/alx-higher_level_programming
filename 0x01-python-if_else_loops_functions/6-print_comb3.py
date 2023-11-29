#!/usr/bin/python3

for first_num in range(0, 10):
    for second_num in range(first_num + 1, 10):
        if first_num == 8 and second_num == 9:
            print("{}{}".format(first_num, second_num))
        else:
            print("{}{}".format(first_num, second_num), end=', ')
