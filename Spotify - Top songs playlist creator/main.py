import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()

SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]

# getting song data
date = input("When would you like to travel to? [YYYY-MM-DD]\n")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")

titles = soup.find_all(class_="chart-element__information__song text--truncate color--primary")
titles = [title.getText() for title in titles]

# connecting to spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# searching songs
song_uris = []
year = date.split("-")[0]
for title in titles:
	result = sp.search(q=f"track:{title} year:{year}", type="track")
	try:
		uri = result["tracks"]["items"][0]["uri"]
		song_uris.append(uri)
	except IndexError:
		print(f"{title} isn't in Spotify. Skipped!!")

# adding to playlist
playlist = sp.user_playlist_create(user_id, f"{date} Billboard 100", public=False, collaborative=False, description='')
playlist_id = playlist["id"]

result = sp.user_playlist_add_tracks(user_id, playlist_id, song_uris, position=None)
print(result)