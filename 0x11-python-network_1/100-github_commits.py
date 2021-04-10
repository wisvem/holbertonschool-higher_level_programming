#!/usr/bin/python3
""" 10. Time for an interview! """

from sys import argv
from requests import post, get, auth

if __name__ == "__main__":
    r_name = argv[1]
    o_name = argv[2]
    _head = {'Accept': 'application/vnd.github.v3+json'}
    url = "https://api.github.com/repos/{}/{}/commits".format(o_name, r_name)
    r = get(url, headers=_head)
    rj = r.json()
    try:
        for i in range(10):
            _sha = rj[i].get('sha')
            _name = rj[i].get('commit').get('author').get('name')
            print("{}: {}".format(_sha, _name))
    except:
        for i in range(len(rj)):
            _sha = rj[i].get('sha')
            _name = rj[i].get('commit').get('author').get('name')
            print("{}: {}".format(_sha, _name))
