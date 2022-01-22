import lyricsgenius


# Use the genius.com song lyric api to get some song lyrics


# Provide a dict with song titles as keys and an artist name and function
# inserts lyrics as values
def get_lyrics(songs, artist):
    for title in songs.keys():
        song = genius.search_song(title, artist)
        # Strip non-ascii characters
        songs[title] = song.lyrics.encode("ascii", "ignore").decode()
    return songs

# Function to save the songs to disk
def save_lyrics():



with open("credentials.txt", "r") as f:
    token = f.read()

genius = lyricsgenius.Genius(token)

# artist = 'Led Zeppelin'
# songs = {'Stairway to Heaven': '', 'Immigrant Song': '', 'Black dog': ''}

artists = ['The White Stripes', 'Nirvana', 'AC/DC']
songs = [
    {'Seven Nation Army': ''},
    {'Smells Like Teen Spirit': '', 'Come as You Are': '', 'Heart-Shaped box': ''},
    {'Back in Black': '', 'Highway to Hell': '', 'Thunderstruck': ''}
]



# songs = get_lyrics(songs, artist)


# Save the song lyrics to disk
# save_lyrics(songs)
