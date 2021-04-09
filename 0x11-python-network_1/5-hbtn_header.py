#!/usr/bin/python3
""" 5. Response header value #1 """

from requests import head
from sys import argv

if __name__ == "__main__":
    r = head(argv[1])
    print(r.headers['X-Request-Id'])
