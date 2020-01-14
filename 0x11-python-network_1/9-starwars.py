#!/usr/bin/python3
"""
Python script that takes in a string and sends
a search request to the Star Wars API
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://swapi.co/api/people/'
    data = {'search': sys.argv[1]}
    r = requests.get(url, data)
    print("Number of results: {}".format(r.json().get('count')))
    for name in r.json().get('results'):
        print(name.get('name'))
