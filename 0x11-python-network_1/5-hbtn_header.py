#!/usr/bin/python3
""" 5. Response header value #1 """

from requests import get
from sys import argv

if __name__ == "__main__":
    r = get(argv[1])
    print(r.headers.get('X-Request-Id'))
