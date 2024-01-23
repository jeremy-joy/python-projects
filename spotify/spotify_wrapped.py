# Short term personal Spotify Wrapped
# Followed along with a tutorial on Youtube
import requests
import spotipy 
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import time
import datetime

from pprint import pprint # to make the output easier to read

DEBUG = 1 # debug lines run when DEBUG == 1

# This would contain my client ID and secret, here they are replaced with 'client_id' and 'client_secret'
SPOTIPY_CLIENT_ID = 'client_id'
SPOTIPY_CLIENT_SECRET = 'client_secret'
SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:9090'
SCOPE = "user-top-read" 

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, 
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope = SCOPE,
                                               open_browser= True))

# top tracks based on a time frame
top_tracks_short = sp.current_user_top_tracks(limit= 20, offset= 0, time_range = "short_term")

# This is of type dict (ie, using key value pairs)
if DEBUG == 1:
    pprint(top_tracks_short)
    print(type(top_tracks_short))

# defining a function to get track ids
def get_track_ids(time_frame):
    track_ids = []
    for song in time_frame['items']:
        # adds song ids to track_ids list
        track_ids.append(song['id'])
    return track_ids

if DEBUG == 1:
    for i in range (100): 
        print('=', end = '')
    print('\n')

track_ids = get_track_ids(top_tracks_short)
if DEBUG == 1:
    pprint(track_ids)

def get_track_features(id):
    meta = sp.track(id)
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']  # gets the first artist
    spotify_url = meta['external_urls']['spotify']
    album_cover = meta['album']['images'][0]['url']
    track_info = [name, album, artist, spotify_url, album_cover]
    return track_info

if DEBUG ==1:
    track_id = '7KqmDr9lTjwXnX5krMIKiC'
    pprint(get_track_features(track_id))



tracks = []
for i in range(len(track_ids)):
    time.sleep(0.5) # small delay is introduced
    track = get_track_features(track_ids[i]) # passes in the track ids one by one
    tracks.append(track)

if DEBUG == 1:
    pprint(tracks)

# Building a data fram to store the tracks
df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist','spotify_url','album_cover'])
if DEBUG == 1:
    print(df.head(5))
