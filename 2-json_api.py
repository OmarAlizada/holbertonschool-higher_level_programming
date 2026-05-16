#!/usr/bin/python3
"""Send POST request to a search API and handle JSON response."""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": q}

    try:
        response = requests.post(url, data=payload)
        json_content = response.json()

        if not json_content:
            print("No result")
        else:
            print("[{}] {}".format(json_content.get("id"), json_content.get("name")))
    except ValueError:
        print("Not a valid JSON")
