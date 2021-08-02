import requests
from bs4 import BeautifulSoup
from datetime import datetime
import password
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

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