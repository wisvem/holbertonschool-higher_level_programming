#!/usr/bin/python3
""" 1. Response header value #0 """

from urllib.request import urlopen
from sys import argv
if __name__ == "__main__":
    with urlopen(argv[1]) as r:
        html = r.info()
        print(html['X-Request-Id'])
