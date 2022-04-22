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


class App:
    def __init__(self):
        self.poems = {}
        self.data = ''
        self.model = None

    def listItems(self):
        """Return a formatted list of the training elements"""
        output = []

        for author in self.poems.keys():
            for title in self.poems[author]:
                output.append(title)


        return output

    def assembleTrainingData(self):
        """Fetch clean and collate training data"""
        for author in self.poems.keys():
            for title in self.poems[author]:
                self.data += getPoem(author, title)

    def buildModel(self):
        """Build the markov chain model"""
        self.assembleTrainingData()
        self.model = Graph(self.data.split())

    def generatePoem(self, length):
        """Return a generated poem of a given length"""
        if self.model is None:
            self.buildModel()

        return self.model.walk(length)
