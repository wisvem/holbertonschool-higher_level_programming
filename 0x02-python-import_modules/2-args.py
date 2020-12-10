#!/usr/bin/python3
if __name__ == "__main__":
    import sys
i = 0
arglen = len(sys.argv)
if arglen < 2:
    print("{} arguments.".format(arglen - 1))
elif arglen == 2:
    print("{} argument:".format(arglen - 1))
else:
    print("{} arguments:".format(arglen - 1))
for arg in sys.argv:
    if (i > 0):
        print("{}:".format(i), arg)
    i = i + 1
