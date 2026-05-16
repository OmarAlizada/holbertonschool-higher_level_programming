#!/usr/bin/python3
"""Fetches a URL and displays information about the response body."""

import urllib.request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    req.add_header("cfclearance", "true")

    with urllib.request.urlopen(req) as response:
        body = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
