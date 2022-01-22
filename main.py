import lyricsgenius
import re
from poetpy import get_poetry


# Clean up the lyrics data removing all text besides the lyrics
def process_lyrics(text: str) -> str:
    return re.sub("\[{1}.*\]{1}|\n+|EmbedShare|URL.*Copy", ' ', text)

# API Testing
def lyric_demo():
    with open('credentials.txt', 'r') as f:
        token = f.read()

    genius = lyricsgenius.Genius(token)

    song = genius.search_song(artist='AC/DC', title='All Screwed Up')

    lyrics = process_lyrics(song.lyrics)

    print(lyrics)

# API Testing
def poetry_demo():
    # List of authors
    authors = get_poetry('author')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
