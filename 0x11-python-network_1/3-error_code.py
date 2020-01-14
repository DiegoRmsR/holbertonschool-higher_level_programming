#!/usr/bin/python3
"""Python script that takes in a URL, sends a request
to the URL and displays the body of the response"""
import urllib.request
import sys


if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.URLError as err:
        print("Error code: {}".format(err.code))
