import xml.etree.ElementTree as ET

# Setup tree and root to parse
print('Welcome to Music Move!\n')
playlist = input('Enter the XML file name: ') + '.xml'
tree = ET.parse(playlist)
root = tree.getroot()


# Finds the name of the song
def get_song_name():
    key1 = 'Name'
    tags = root.iter()
    songs = []
    for node in tags:
        if key1 == node.text:
            next_node = next(tags)
            songs.append(next_node.text)

    del songs[-1]  # Deletes PlayList name
    return songs


# Removes Feature from song name
def remove_feat_from_song(songname):
    result = []
    for song in songname:
        start = song.find('(')
        if start != -1:
            result.append(song[0:start])
        else:
            result.append(song)
    return result


# Removes Feature from album name
def remove_feat_from_album(album_name1):
    result = []
    for song in album_name1:
        start = song.find('(')
        if start != -1:
            result.append(song[0:start])
        else:
            result.append(song)
    return result


# Finds the Artist of the song
def get_artist_name():
    key2 = 'Artist'
    tags = root.iter()
    artists = []
    for node in tags:
        if key2 == node.text:
            next_node = next(tags)
            artists.append(next_node.text)
    return artists


# Finds the album name
def get_album_name():
    key3 = 'Album'
    tags = root.iter()
    songs = []
    for node in tags:
        if key3 == node.text:
            next_node = next(tags)
            songs.append(next_node.text)
    return songs