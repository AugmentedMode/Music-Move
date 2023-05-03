from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util
import numpy as np

username = ""

# Spotify Token Access
client_id = ""
client_secret = ""
if not client_id or not client_secret or not username:
    print('ERROR: One of client_id, client_secret, or username is unset in spotify_accessor.py.')
    exit(1)

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# Create Spotify playlist ID
def create_playlist(username):

    username = username
    playlist_name = input('Enter playlist name: ')

    token = util.prompt_for_user_token(username=username, scope='playlist-modify-public', client_id=client_id,
                                       client_secret=client_secret, redirect_uri="http://localhost:8888/callback")

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        playlists = sp.user_playlist_create(username, playlist_name)
        return playlists['id']


# Get trackID for songs
def get_track_id(song_name1, artist_name1, album_name1):
    print("Adding songs to playlist!")
    id_list = []
    my_array = []
    album_list = []
    song_list = []

    i = 0
    while i < len(song_name1):
        artist = artist_name1[i]
        track = song_name1[i]

        try:
            track_id = sp.search(q='artist:' + artist + ' track:' + track, type='track')
        except spotipy.exceptions.SpotifyException:
            print(f'WARNING: Could not find "{track}" in Spotify.')
            continue
        for songsID in track_id['tracks']['items']:
            id_list.append(songsID['id'])
        if not id_list:
            album_list.append(album_name1[i])
            song_list.append(song_name1[i])
        else:
            my_array.append(id_list[0])
        id_list = []
        i += 1
    return my_array, album_list, song_list


# Get trackID for songs
def get_missing_track_id(missing_albums1, missing_tracks1):
    id_list = []
    my_array = []

    i = 0
    while i < len(missing_tracks1):
        album = missing_albums1[i]
        track = missing_tracks1[i]

        track_id = sp.search(q='album:' + album + ' track:' + track, type='track')
        for songsID in track_id['tracks']['items']:
            id_list.append(songsID['id'])
        if not id_list:
            print('Could not add: ' + missing_tracks1[i])
        else:
            my_array.append(id_list[0])
        id_list = []
        i += 1
    return my_array

def add_more_than_100_songs_to_playlist(username, playlist_id, track_ids):
    #split array in size of 50
    track_id_chunks = np.array_split(track_ids, len(track_ids)/50)
    for track_id_chunk in track_id_chunks:
        add_songs_to_playlist(username, playlist_id, track_id_chunk)

# Add songs to Spotify Playlist
def add_songs_to_playlist(username, playlist_id, track_ids):

    username = username
    playlist_id = playlist_id
    track_ids = track_ids

    token = util.prompt_for_user_token(username=username, scope='playlist-modify-public', client_id=client_id,
                                       client_secret=client_secret, redirect_uri="http://localhost:8888/callback")

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False

        results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
        print('Finished transferring playlist')
        return results


def add_song_ids(multiple_tracks1, more_tracks1):
    result = multiple_tracks1 + more_tracks1
    return result