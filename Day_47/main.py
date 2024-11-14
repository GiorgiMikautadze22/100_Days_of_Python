import os
from dotenv import load_dotenv
import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy import SpotifyOAuth

load_dotenv()

date = input("What year year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

api_url = f"https://www.billboard.com/charts/hot-100/{date}"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=api_url, headers=header)
website_html = response.text

soap = BeautifulSoup(website_html, "html.parser")
song_names_spans = soap.select("li ul li h3")[0:10]

songs = [song.getText().strip() for song in song_names_spans]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://developer.spotify.com/dashboard",
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_SECRET_KEY"),
        show_dialog=True,
        cache_path="token.txt",
        username="giorgi mikautadze",
    )
)

user_id = sp.current_user()["id"]

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)