# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import argparse

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

def addWordsFromStrToDict(str, bag):
    words = str.split()
    for word in words:
        if word not in bag:
            bag[word] = 1
        else:
            bag[word] += 1


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Find a user\'s top words from recent tweets')
    parser.add_argument('-u', '--user', default='BarackObama')
    args = parser.parse_args()

    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print "OAUTH_TOKEN: " + token
        print "OAUTH_TOKEN_SECRET: " + secret
        print
    
    else:

        query_params = {'screen_name': args.user,
                        'count': 200
                    }
        oauth = get_oauth()

        endpoint = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
        response = requests.get(endpoint, params=query_params, auth=oauth)  
        data = response.json()

        wordBag = {}

        for tweet in response.json():
            tweetstr = tweet['text'].encode('ascii', 'ignore')
            addWordsFromStrToDict(tweetstr, wordBag)

        print "count\tword"
        sortedBag = sorted(wordBag.items(), key=lambda tup: tup[1], reverse=True)
        for word in sortedBag[0:9]:
            print "{0}\t{1}".format(word[1], word[0])
