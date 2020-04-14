#!/usr/bin/python3

"""script that takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response"""

if __name__ == "__main__":
    from urllib import request, parse
    import sys

    data = parse.urlencode({'email': sys.argv[2]}).encode()
    req = request.Request(sys.argv[1], data=data, method='POST')
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
