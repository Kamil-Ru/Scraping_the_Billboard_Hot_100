import requests
from bs4 import BeautifulSoup
from datetime import datetime
import password
import spotipy
from spotipy.oauth2 import SpotifyOAuth

USER = password.USER

Spotify_ID = password.Client_ID
Spotify_password = password.Client_Secret

while True:
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD\n")
    try:
        datetime.fromisoformat(date)
    except ValueError:
        print("Date should be in format: YYYY-MM-DD")
    else:
        break

URL = "https://www.billboard.com/charts/hot-100/"
URL_and_date = URL + date

print(URL_and_date)

response = requests.get(URL_and_date)
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")

all_music = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
print(all_music)

all_music_list = [song.get_text() for song in all_music]

print(all_music_list)

scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, username=USER))

year = date.split("-")[0]
print(year)

track_URI_list = []

for music in all_music_list:
    q = f"track: {music} year: {year}"
    search_track = sp.search(q=q, limit=1, type="track")
    print(search_track)
    try:
        track_uri = search_track["tracks"]["items"][0]["uri"]
        track_URI_list.append(track_uri)
        print(track_uri)
    except IndexError:
        print("NONE")


new_playlist = sp.user_playlist_create(user=USER, name=f"{date} Billboard 100", public=False)
new_playlist_ID = new_playlist["id"]

sp.playlist_add_items(playlist_id=new_playlist_ID, items=track_URI_list, position=None)