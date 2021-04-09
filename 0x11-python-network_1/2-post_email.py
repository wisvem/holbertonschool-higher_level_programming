#!/usr/bin/python3
""" 2. POST an email #0 """

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    _data = urlencode({'email': argv[2]}).encode('utf-8')
    req = Request(url, data=_data)  # this makes the method "POST"
    with urlopen(req) as r:
        html = r.read()
        print('{}'.format(html.decode('utf-8')))
