#!/usr/bin/python3
""" 1. Response header value #0 """

from urllib.request import urlopen
from sys import argv
with urlopen('{}'.format(argv[1])) as r:
    html = r.info()
    print(html['X-Request-Id'])
