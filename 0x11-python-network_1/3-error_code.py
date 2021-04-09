#!/usr/bin/python3
""" 3. Error code #0 """

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(argv[1]) as r:
            html = r.read()
            print(html.decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
