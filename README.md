# Spotipy-Stream-Overlay
A browser source stream overlay using python and html

# Requirements
You need to download [Python3](https://www.python.org/downloads/) to run the script file.

After python is installed, using PIP, download spotipy

```bash
pip3 install spotipy
```

Once spotipy is installed you need to edit the client_id and client_secret within the get_track.py.

```
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR CLIENT ID",
                                               client_secret="YOUR CLIENT SECRET",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-read-currently-playing"))
```
To find your client_id and client_secret you need to login at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) and create a new app. When the app has been created change the Redirect URls to `http://localhost:8888/callback`

![alt text](https://cdn.discordapp.com/attachments/807327456494354514/810295728596713552/unknown.png)
