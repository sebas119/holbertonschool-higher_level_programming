#!/usr/bin/python3

"""Python script that takes in 3 strings and sends a
search request to the Twitter API"

The first argument must be the Consumer Key (API Key)
The second argument must be the Consumer Secret (API Secret)
The third argument must be the search string
"""

if __name__ == "__main__":

    from requests import get, post
    from sys import argv
    from base64 import b64encode

    api_key = '9U79aFfXb2AGxkNGXNEtZzN9X'
    api_secret = '9hCPFl23d1GzuLnZiCHGoT2PWKJql38AXleRUUQaOVP8jDwhnf'
    api_tokens = "{}:{}".format(argv[1], argv[2])
    # 1. Encode base64
    encode64_api_tokens = (
        b64encode(api_tokens.encode('ascii'))).decode("utf-8")
    # Endpoint to auth and generate the access_token
    url = "https://api.twitter.com/oauth2/token"
    headers = {
        'Authorization': "Basic {}".format(encode64_api_tokens),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    body = {'grant_type': 'client_credentials'}
    # 2. Make the post request to obtain a bearer token
    r = post(url, data=body, headers=headers)
    bearer_token = r.json().get('access_token')
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    headers_search = {'Authorization': "Bearer {}".format(bearer_token)}
    payload = {'q': argv[3], 'count': '5'}
    # 3. Make an API requests with the bearer token to search tweets
    r = get(url, headers=headers_search, params=payload)
    tweets_data = r.json().get('statuses')

    for elem in tweets_data:
        owner = elem.get('user').get('name')
        print("[{}] {} by {}".format(
            elem.get('id'), elem.get('text'), owner))
