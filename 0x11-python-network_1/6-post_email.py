#!/usr/bin/python3
""" 6. POST an email #1 """

from requests import post, get
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    _data = {'email': argv[2]}
    r = post(url, data=_data)
    print(r.text)
