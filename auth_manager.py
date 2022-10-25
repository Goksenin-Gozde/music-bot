import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def getSpotifyClient():
    auth_manager = SpotifyClientCredentials()
    return spotipy.Spotify(auth_manager=auth_manager)