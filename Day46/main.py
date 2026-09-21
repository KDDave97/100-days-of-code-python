import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
import os

client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                    client_secret=client_secret,
                                                    redirect_uri="http://127.0.0.1:3000",
                                                    scope = "user-library-read playlist-modify-private playlist-read-private"))

response = requests.get("https://www.billboard.com/charts/hot-100/")
hot100 = response.text

soup = BeautifulSoup(hot100, "html.parser")

artist_name= []
song_name = []

top100_box = soup.find_all(name="li", class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-padding-l-050 lrv-u-padding-l-00@mobile-max u-max-width-397")

for artist_ in top100_box:
     song_name.append(artist_.find(name="h3").getText().strip())
     artist_name.append(artist_.find(name="span").getText().strip())

results = []
track_uris = []

for i in range(len(song_name)):
    results.append(spotify.search(q=f"track:{song_name[i]} artist:{artist_name[i]}", type="track", limit=10))

for uri in results:
    track_uris.append(uri["tracks"]["items"][0]["uri"])

playlists = spotify.current_user_playlists(limit=50, offset=0)
current_playlist = playlists["items"][0]["id"]

spotify.playlist_add_items(playlist_id=current_playlist, items=track_uris)


#spotify.current_user_playlist_create(name="Today's Hot 100", public=False, collaborative=False, description="Made with Python for the 100 days of Code in python course")



