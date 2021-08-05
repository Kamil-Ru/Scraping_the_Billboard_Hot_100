import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import password

Spotify_ID = password.Client_ID
Spotify_password = password.Client_Secret
redirect_URI = password.redirect_URI

spotify = spotipy.oauth2.SpotifyOAuth(client_id=Spotify_ID, client_secret=Spotify_password, redirect_uri=redirect_URI, scope=playlist-modify-private)
access_token = spotify.get_access_token()

print(access_token)

authorize_url = spotify.get_authorize_url()


print(authorize_url)
