#!/usr/bin/python3
""" 0. What's my status? #0 """

from urllib.request import urlopen
with urlopen('https://intranet.hbtn.io/status') as r:
    html = r.read()
    print("Body response:")
    print("    - type: {}".format(type(html)))
    print("    - content: {}".format(html))
    print("    - utf8 content: {}".format(html.decode("utf-8")))
