# Spotipy-Stream-Overlay
A browser source stream overlay using python and html

# Requirements
You need to download [Python3](https://www.python.org/downloads/) to run the script file.

After python is installed, using PIP, download spotipy

```bash
pip3 install spotipy
```

Once spotipy is installed you need to edit the clientid and clientsecret within the get_track.py

```
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR CLIENT ID",
                                               client_secret="YOUR CLIENT SECRET",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-read-currently-playing"))
```
