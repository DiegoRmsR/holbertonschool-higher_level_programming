#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    bad_r = requests.get(sys.argv[1])
    if bad_r.status_code > 309:
        print("Error code: {}".format(bad_r.status_code))
    else:
        print(bad_r.text)
