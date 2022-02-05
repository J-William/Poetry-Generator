from poetpy import get_poetry
from Graph import Graph


def getAvailableAuthors():
    """Return a list of currently hosted authors from poet-db"""
    return list(get_poetry('author')['authors'])


def getAuthorTitles(author):
    """Return all listed titles of a given author"""
    return get_poetry('author', author, 'title')


def getPoem(author, title):
    """Return the content of a given poem"""
    txt = get_poetry('author,title', author+';'+title, 'lines', 'text')
    # Cleanup the text
    txt = txt.replace('--', '')
    txt = txt.replace('lines', '')
    return txt.lower()


def getSong(artist, song):
    """Return the lyrics of a given song"""
    pass


class App:
    def __init__(self):
        self.poems = {}
        self.songs = {}
        self.data = ''
        self.model = None

    def listItems(self):
        """Return a formatted list of the training elements"""
        output = []

        for author in self.poems.keys():
            for title in self.poems[author]:
                output.append(author+' -- '+title)

        for artist in self.songs.keys():
            for song in self.songs[artist]:
                output.append(artist+' -- '+song)

        return output

    def assembleTrainingData(self):
        """Fetch clean and collate training data"""
        for author in self.poems.keys():
            for title in self.poems[author]:
                self.data += getPoem(author, title)

        for artist in self.songs.keys():
            for song in self.songs[artist]:
                self.data += getSong(artist, song)

    def buildModel(self):
        """Build the markov chain model"""
        self.assembleTrainingData()
        self.model = Graph(self.data.split())

    def generatePoem(self, length):
        """Return a generated poem of a given length"""
        if self.model is None:
            self.buildModel()

        return self.model.walk(length)
