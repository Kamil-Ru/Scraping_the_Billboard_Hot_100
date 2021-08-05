import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import password


Spotify_ID = password.Client_ID
Spotify_password = password.Client_Secret
redirect_URI = password.redirect_URI
TOKEN = password.TOKEN

USER = password.USER


import spotipy
from spotipy.oauth2 import SpotifyOAuth


import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-library-read user-read-playback-state playlist-modify-private", username=USER))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

# p = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Spotify_ID,
#                                               client_secret=Spotify_password,
#                                               redirect_uri=redirect_URI,
#                                               scope="user-read-private"))

# results = sp.current_user_saved_tracks()
#  for idx, item in enumerate(results['items']):
#      track = item['track']
#      print(idx, track['artists'][0]['name'], " – ", track['name'])
#

user_name = sp.current_user()
print(user_name)

played = sp.currently_playing()
print(played)

q = "track: This Is America year: 2018"

search_track = sp.search(q=q, limit=1, type="track")
print(search_track)

print(type(search_track))


track_name = search_track["tracks"]["items"][0]["name"]
track_URL = search_track["tracks"]["items"][0]["external_urls"]["spotify"]
track_uri = search_track["tracks"]["items"][0]["uri"]

print(track_name)
print(track_URL)
print(track_uri)

sp.user_playlist_create(user=USER, name="TEST", public=False)

#delete this
device = sp.devices()
print(device)

list_playlist = sp.current_user_playlists()
print(list_playlist)

for item in list_playlist["items"]:
    print(item["name"])
    if item["name"] == "TEST":
        id = item["id"]
        print("JEST")

print(id)


# sp.playlist_add_items(playlist_id="TEST", items=track_uri)