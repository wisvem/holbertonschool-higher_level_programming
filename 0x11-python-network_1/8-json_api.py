#!/usr/bin/python3
""" 8. Search API """

from sys import argv
from requests import post, get

if __name__ == "__main__":
    try:
        _data = {'q': argv[1]}
    except:
        _data = {'q': ""}
    url = 'http://0.0.0.0:5000/search_user'
    try:
        r = post(url, data=_data)
        rj = r.json()
        if (len(rj) is not 0):
            print("[{}] {}".format(rj.get('id'), rj.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
