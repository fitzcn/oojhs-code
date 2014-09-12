"""
This code is from Thomas Sileo:
http://thomassileo.com/blog/2013/01/25/using-twitter-rest-api-v1-dot-1-with-python/


A quick guide on how to retrieve your Twitter data with Python (from scripts/command line, without setting up a web server) and Twitter REST API v1.1.

Requirements

We will use requests along with requests-oauthlib.

If you haven't heard about requests yet, it provides a pythonic way to make complex HTTP requests, and handles difficult tasks like authentication.

Accessing Twitter API

Here is the code, followed by the explanations:
"""

# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "YOUR_CONSUMER_KEY"
CONSUMER_SECRET = "YOUR CONSUMER_SECRET"

OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""


def setup_oauth():
    """Authorize your app via identifier."""
    # Request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)

    resource_owner_key = credentials.get('oauth_token')[0]
    resource_owner_secret = credentials.get('oauth_token_secret')[0]

    # Authorize
    authorize_url = AUTHORIZE_URL + resource_owner_key
    print 'Please go here and authorize: ' + authorize_url

    verifier = raw_input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials.get('oauth_token')[0]
    secret = credentials.get('oauth_token_secret')[0]

    return token, secret


def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print "OAUTH_TOKEN: " + token
        print "OAUTH_TOKEN_SECRET: " + secret
        print
    else:
        oauth = get_oauth()
        r = requests.get(url="https://api.twitter.com/1.1/statuses/mentions_timeline.json", auth=oauth)
        print r.json()

"""
In order to access your own data, you must create an application, and generate your own access token, more informations on the Twitter API Getting Started.

Go to https://dev.twitter.com/ and register a new appp, fill everything but leave the Callback URL empty if you want call the API without setting up a web server.

The API will give us an URL to get an identifier, so we don't need callback.

Save the consumer key and consumer secret, set the two constants at the top of mytweets.py: CONSUMER_KEY and CONSUMER_SECRET.

Next to generate the OAUTH tokens, just run mytweets.py.

$ sudo pip install request request_oauthlib
$ wget https://gist.github.com/raw/4637864/9ea056ffbe5bb88705e95b786332ae4c0fd7554c/mytweets.py
$ python mytweets.py
Go to the URL, enter your identifier, set OAUTH_TOKEN and OAUTH_TOKEN_SECRET. Now you can run mytweets.py again.

$ python mytweets.py
Now, you should see your last mentions !

You can get the official Twitter REST API documentation here.

Please don't hesitate to leave feedback, criticism, or to ask whatever questions you have.
"""
