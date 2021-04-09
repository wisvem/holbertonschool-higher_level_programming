#!/usr/bin/python3
""" 7. Error code #1 """

from sys import argv
from requests import post, get, HTTPError

if __name__ == "__main__":
    r = get(argv[1])
    if r:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
