#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1

    if length == 0:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
    else:
        print("{} arguments:".format(length))

    if length >= 1:
        length = 0
        for arg in sys.argv:
            if length != 0:
                print('{}: {}'.format(length, arg))
            length += 1
