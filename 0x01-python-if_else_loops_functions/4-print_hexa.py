#!/usr/bin/python3

for a in range(99):
    print("{} = 0x{}".format(a, hex(a)[2:]) if a < 16 \
else "{} = 0x{}".format(a, hex(a)[2:]))
