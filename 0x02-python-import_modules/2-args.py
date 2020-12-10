#!/usr/bin/python3
if __name__ == "__main__":
    import sys
i = 0
if len(sys.argv) < 2:
    print("{} Arguments.".format(len(sys.argv) - 1))
else:
    print("{} Arguments:".format(len(sys.argv) - 1))
for arg in sys.argv:
    if (i > 0):
        print("{}: {}".format(i, arg))
    i = i + 1
