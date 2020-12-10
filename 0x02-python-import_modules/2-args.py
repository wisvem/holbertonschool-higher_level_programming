#!/usr/bin/python3
if __name__ == "__main__":
    import sys
i = 0
print("{} Arguments".format(len(sys.argv) - 1), end="")
print(".") if len(sys.argv) < 2 else print(":")
for arg in sys.argv:
    if (i > 0):
        print("{}: {}".format(i, arg))
    i = i + 1
