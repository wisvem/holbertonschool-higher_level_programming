#!/usr/bin/python3
""" 5. Response header value #1 """

from requests import get
from sys import argv

if __name__ == "__main__":
    r = get('https://intranet.hbtn.io/status')
    print(r.headers['X-Request-Id'])
