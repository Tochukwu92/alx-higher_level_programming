#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    i = 0
    while True:
        try:
            result = result + (a ** b) / i
        except:
            if i > 100:
                raise ValueError('Too far')
            result = result + (a + b)
        finally:
            i += 1
            if i > 100:
                break
    return result


