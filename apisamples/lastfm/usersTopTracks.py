import requests
import json
import argparse

parser = argparse.ArgumentParser(description='Find a user\'s top tracks')
parser.add_argument('-u', '--user', default='RJ')
args = parser.parse_args()

query_params = { 'api_key': '',
				 'method': 'user.gettoptracks',
				 'user': args.user,
				 'period': '3month',
				 'limit': 10,
				 'format': 'json'
		 		}

endpoint = 'http://ws.audioscrobbler.com/2.0'
response = requests.get(endpoint, params=query_params)
data = json.loads(response.text)


title = "TOP 10 TRACKS " + args.user.upper() + " LISTENS TO:"
print title

#print data

i = 1
for track in data['toptracks']['track']:
	print i, track['name'], track['artist']['name']
	i+=1


