import spotipy
import os
import time
import json
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR CLIENT ID",
                                               client_secret="YOUR CLIENT SECRET",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-read-currently-playing"))

refimageurl = ("null")
i = 1
while i < 2:
    # Getting song info
    trackinfo = sp.current_user_playing_track()
    # Finding song from json file
    track = trackinfo['item']['name']
    artist = trackinfo['item']['artists'][0]['name']
    imageurl = trackinfo['item']['album']['images'][0]['url']
    if imageurl == refimageurl:
        print ('images are the same')
        time.sleep(4)
    else:
        os.system ("rm webpage/img/image")
        os.system("wget " +imageurl+ " -P webpage/img/")
        files = os.listdir("webpage/img/")
        files = str(files)
        files = files.replace('[', '')
        files = files.replace(']', '')
        print (files)
        os.system ("mv webpage/img/"+ files + " webpage/img/image")
        refimageurl = imageurl

        # Change html text
        os.system('sed -i "/<h1>/c\<h1>'+track+'" webpage/index.html')
        os.system('sed -i "/<h2>/c\<h2>'+artist+'" webpage/index.html')
        #time.sleep(1)
        #os.system ("rm webpage/img/image")





## Prints metadata to file to search
# f = open("metadata.txt", "a")
# f.write(json.dumps(trackinfo, sort_keys=True, indent=4))
# f.close()

# prints out track info and image url
# track = trackinfo['item']['name']
# artist = trackinfo['item']['artists'][0]['name']
# print('Currently playing ' + track + ' - ' + artist)