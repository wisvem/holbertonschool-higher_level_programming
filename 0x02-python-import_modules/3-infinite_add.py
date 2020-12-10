#!/usr/bin/python3
if __name__ == "__main__":
    import sys
res, i = 0, 0
for arg in sys.argv:
    if (i > 0):
        res = res + int(arg)
    i = i + 1
print(res)
