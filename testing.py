import lyricsgenius
import re
from poetpy import get_poetry
from Graph import Graph


# Clean up the lyrics data removing all text besides the lyrics
def process_lyrics(text: str) -> str:
    return re.sub("\[{1}.*\]{1}|\n+|EmbedShare|URL.*Copy|\)|\(", ' ', text)


# API Testing
def lyric_demo(artist, songs):
    with open('credentials.txt', 'r') as f:
        token = f.read()

    genius = lyricsgenius.Genius(token)

    # songs = ['All Screwed Up', 'Highway to Hell', 'Thunderstruck']
    lyrics = ''

    for song in songs:
        data = genius.search_song(artist=artist, title=song)
        lyrics += process_lyrics(data.lyrics)

    return lyrics.lower()


# API Testing
def poetry_demo(author):
    # List of authors
    # authors = get_poetry('author')
    txt = get_poetry('author', author, 'lines', 'text')
    txt = txt.replace('--', '')
    txt = txt.replace('lines', '')

    return txt.lower()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    qArtist = 'AC/DC'
    qSongs = ['All Screwed Up', 'Highway to Hell', 'Thunderstruck']
    qAuthor = 'William Shakespeare'

    lyrics = lyric_demo(qArtist, qSongs)

    poem = poetry_demo(qAuthor)

    # Concatenate lyrics and poetry
    txt = lyrics + ' ' + poem

    src = txt.split()

    myg = Graph(src)
    # for v in myg.vertices:
    #     print(v.val)
    #     print(v.edges)

    while True:
        if input('Continue? ') not in ['y', 'Y']:
            break
        print(myg.generatePoem(10))
