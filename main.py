import requests
from bs4 import BeautifulSoup
from datetime import datetime
import password
import spotipy
from spotipy.oauth2 import SpotifyOAuth

USER = password.USER

# Input user date
while True:
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD\n")
    try:
        datetime.fromisoformat(date)
    except ValueError:
        print("Date should be in format: YYYY-MM-DD")
    else:
        break

# searching track on www.billboard.com
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")
all_music = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

all_song_list = [song.get_text() for song in all_music]

# Login to Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-public", username=USER))

# Getting year from user date
year = date.split("-")[0]

# Creating list URI of searching music
track_URI_list = []
for song in all_song_list:
    q = f"track: {song} year: {year}"
    search_track = sp.search(q=q, limit=1, type="track")
    if not search_track["tracks"]["items"]:
        print(f"{song} doesn't exist in Spotify. Skipped.")
    else:
        track_uri = search_track["tracks"]["items"][0]["uri"]
        track_URI_list.append(track_uri)

# Creating empty playlist on Spotify
new_playlist = sp.user_playlist_create(user=USER, name=f"{date} Billboard 100", public=False)
new_playlist_ID = new_playlist["id"]

# Adding list URI of music to playlist
sp.playlist_add_items(playlist_id=new_playlist_ID, items=track_URI_list, position=None)