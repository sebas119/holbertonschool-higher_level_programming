#!/usr/bin/python3

"""script that takes your Github credentials (username and password) and uses
the Github API to display your id"""

if __name__ == "__main__":

    from requests import get, auth
    from sys import argv

    r = get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(r.json().get('id'))
