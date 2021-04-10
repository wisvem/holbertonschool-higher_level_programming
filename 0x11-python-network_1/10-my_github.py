#!/usr/bin/python3
""" 9. My GitHub! """

from sys import argv
from requests import post, get, auth

if __name__ == "__main__":
    _user = argv[1]
    _token = argv[2]
    url = 'https://api.github.com/user'
    r = get(url, auth=(_user, _token))
    rj = r.json()
    print(rj.get('id'))
