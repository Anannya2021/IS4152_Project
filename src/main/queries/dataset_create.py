import spotipy
import spotipy.util as util
import spotipy.oauth2 as oauth2
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
​
CLIENT_ID = ""
CLIENT_SECRET = ""
​
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
​
#Top 100 US songs playlist id
american_playlist_id = "37i9dQZEVXbLRQDuF5jeBp"
#Top 50 Hindi songs playlist id
indian_playlist_id = "2PstCwMHBY9Lxt1a4CDUpT"
#Top 500 Chinese popular songs id
chinese_playlist_id = "3T7Yri0pmUdyj1AEGN3KjO"
​
def analyze_playlist(creator, playlist_id):
    
    # Create empty dataframe
    playlist_features_list = ["artist", "album", "track_name", 
                             "danceability", "energy", "key", "loudness", "mode", "speechiness",
                             "instrumentalness", "liveness", "valence", "tempo"]
    playlist_dataframe = pd.DataFrame(columns = playlist_features_list)
    
    playlist_features = {}
    
    # Loop through every track in the playlist, extract features and append the features to the playlist df
    playlist = sp.user_playlist_tracks(creator, playlist_id)["items"]
    #print(playlist)
    for track in playlist:
        # Get metadata
        playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
        playlist_features["album"] = track["track"]["album"]["name"]
        playlist_features["track_name"] = track["track"]["name"]
        # Get audio features
        audio_features = sp.audio_features([track["track"]["id"]])[0]
        for feature in playlist_features_list[3:]:
            playlist_features[feature] = audio_features[feature]
        # Concat the header and the rows dfs
        track_dataframe = pd.DataFrame(playlist_features, index = [0])
        playlist_dataframe = pd.concat([playlist_dataframe, track_dataframe], ignore_index = True)
        
    return playlist_dataframe
​
american_songs = analyze_playlist("spotify",american_playlist_id)
american_songs = american_songs.sample(n=50)
indian_songs = analyze_playlist("Musico Playlists",indian_playlist_id)
indian_songs = indian_songs.sample(n=50)
chinese_songs = analyze_playlist("Eric",chinese_playlist_id)
chinese_songs = chinese_songs.sample(n=50)
songs = pd.concat([american_songs, indian_songs, chinese_songs], ignore_index=True, sort=False)
print(len(songs))
print(len(american_songs))
print(len(indian_songs))
print(len(chinese_songs))
​
#WRITING TO CSV FILE
songs.to_csv('audio_features.csv',encoding='utf-8')
