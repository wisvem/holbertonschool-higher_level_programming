#!/usr/bin/python3
def magic_string():
    count = 0
    setattr(magic_string, "count", count+1)
    print(count)
    return "Holberton"
