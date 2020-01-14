#!/usr/bin/python3
"""
Python script that takes your Github credentials
(username and password) and uses the Github API
to display your id
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    paswd = sys.argv[2]
    r = get(url, auth=auth.HTTPBasicAuth(user, paswd))
    print(r.json().get('id'))
