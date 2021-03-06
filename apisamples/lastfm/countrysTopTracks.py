import requests
import json
import argparse

parser = argparse.ArgumentParser(description='Find a country\'s top artists')
parser.add_argument('-c', '--country', default='United States')
args = parser.parse_args()

query_params = { 'api_key': '',
				 'method': 'geo.gettoptracks',
				 'country': args.country,
				 'limit': 10,
				 'format': 'json'
		 		}

endpoint = 'http://ws.audioscrobbler.com/2.0'
response = requests.get(endpoint, params=query_params)
data = json.loads(response.text)


title = "TOP 10 ARTISTS IN " + args.country.upper()
print title


i = 1
for track in data['toptracks']['track']:
	print i, track['name'], track['artist']['name']
	i+=1

