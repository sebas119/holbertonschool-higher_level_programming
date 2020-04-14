#!/usr/bin/python3

"""script that takes in a URL and an email address, sends a POST request to
the passed URL with the email as a parameter, and finally displays the body
of the response."""

if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])

    if r.status_code == requests.codes.ok:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
