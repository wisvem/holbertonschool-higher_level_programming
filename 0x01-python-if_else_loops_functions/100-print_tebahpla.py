#!/usr/bin/python3
for i in range(25, -1, -1):
    x = i + ord('A')
    if i % 2 == 1:
        x = x+32
    print("{}".format(chr(x)), end="")
