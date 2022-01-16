# Use the poetpy wrapper to get poetry from poetrydb api: https://poetrydb.org/index.html
import string
import poetpy
import os



def download_author(author):
    # Get the authors poems
    poems = poetpy.get_poetry('author', author, 'lines')
    # Write the lines to a text files
    for poem in poems:
        for line in poem['lines']:
            with open('poetry/{}.txt'.format(author), 'a') as f:
                f.write(line+'\n')


def extract_words(text_path):
    with open(text_path, 'r') as f:
        text = f.read()

    # Standardize and cleanup the text
    for e in string.punctuation:
        text = text.replace(e, ' ')
    text = ' '.join(text.split())
    text = text.lower()

    # Return the text as a list of words
    return text.split()



if __name__ == '__main__':
    # Download a few authors works
    authors = ['Emily Dickinson', 'William Shakespeare', 'William Wordsworth']
    for author in authors:
        download_author(author)

    # Extract the words from the poems and build a list
    words = []
    for file in os.listdir('poetry/'):
        words.extend(extract_words('poetry/{}'.format(file)))






