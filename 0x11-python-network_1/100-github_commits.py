#!/usr/bin/python3

"""Print all commits by: `<sha>: <author name>` (one by line)
using Github API"""

if __name__ == "__main__":

    from requests import get, auth
    from sys import argv

    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits?per_page=10".format(
        owner, repo)
    r = get(url)
    for elem in r.json():
        arr_author = (elem.get('commit')).get('author')
        print("{}: {}".format(elem.get('sha'), arr_author.get('name')))
