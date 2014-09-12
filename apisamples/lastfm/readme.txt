These three scripts all work from the command line, with specified cl arguments.

First, you must have a lastfm account and sign up on the API page for an app.

http://www.last.fm/api/accounts

After you create an API account/app, it will have an API key. Add the key as a string to any of the query_params statements in the code. (i.e. replace the empty string with your api key)

Run the scripts and enjoy exploring!


Specify a country through the command line by (default is United States):
$ python countrysTopTracks.py -c Brazil
$ python countrysTopArtists.py -c Brazil

Specify a user through the command line by (default is Richard Jones, inventor of AudioScrobbler):
$ python usersTopTracks.py -u mainstream
(mainstream is Martin Stiksel, another one of the three creators of lastfm)