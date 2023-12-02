#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_len = len(sys.argv) - 1
    if arg_len != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)

    sign = ['+', '-', '*', '/']
    op = sys.argv[2]
    if op not in sign:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == '+':
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    elif op == '-':
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
    elif op == '*':
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
    else:
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
