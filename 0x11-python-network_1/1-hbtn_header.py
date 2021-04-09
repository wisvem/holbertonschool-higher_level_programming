#!/usr/bin/python3
""" 1. Response header value #0 """

from urllib.request import urlopen
from sys import argv
with urlopen(argv[1]) as r:
    html = r.headers
    print(html['X-Request-Id'])
