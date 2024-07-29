#!/usr/bin/python3
"""
    A a Python script that takes in a URL,
    sends a request to the URL and displays the value
    of the X-Request-Id variable found in the header of the response.
"""


if __name__ == "__main__":
    import sys
    import urllib.request

    arg_url = sys.argv[1]
    req = urllib.request.Request(arg_url)
    with urllib.request.urlopen(req) as res:
        print(dict(res.headers).get('X-Request-Id'))
