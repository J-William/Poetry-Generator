import lyricsgenius


with open("credentials.txt", "r") as f:
    token = f.read()

genius = lyricsgenius.Genius(token)

artist = genius.search_artist("The Beatles", max_songs=1, sort="title")

print(artist.songs)
