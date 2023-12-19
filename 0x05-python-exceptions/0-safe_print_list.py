#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    lenght = 0
    for lists in range(0, x):
        try:
            print(my_list[lists], end="")
            lenght += 1
        except IndexError:
            break
    print()
    return lenght
