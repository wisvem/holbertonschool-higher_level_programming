#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 122):
            x = 32
        else:
            x = 0
        print(chr(ord(c)-x), end='')
    print()
