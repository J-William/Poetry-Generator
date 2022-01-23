class Graph:
    """
    Represents a Markov chain model as a list of vertices
    """
    class Vertex:
        """
        Represents a node in the graph contains a dictionary of
        edges directed at other vertices
        """

        def __init__(self, x: str):
            self.val = x
            self.edges = {}

        def addEdge(self, word: str):
            if word in self.edges.keys():
                self.edges[word] += 1
            else:
                self.edges[word] = 1

    def __init__(self, src: []):
        self.vertices = []
        self.build(src)

    def find(self, data: str) -> int:
        """ Searches for a vertex returns the index or -1 if not present. """

        for vertex in self.vertices:
            if vertex.val == data:
                return self.vertices.index(vertex)
        return -1

    def build(self, src: []) -> []:
        """
        Takes a list of words and builds a Markov chain model
        represented as a list of vertices

        """
        for i in range(len(src)-1):
            index = self.find(src[i])

            if index == -1:
                # The word is not represented by a vertex, add it
                new_vertex = self.Vertex(src[i])
                new_vertex.addEdge(src[i+1])
                self.vertices.append(new_vertex)
                index = self.find(src[i])
            else:
                # Add edge to the vertex
                self.vertices[index].addEdge(src[i+1])





    def randomWalk(self, length: int):
        """
        Returns a string(poem) built from a walk along the graph for a given
        number of steps(length)

        :param length: The number of steps(words) to return
        :return poem:  The string representing a generated poem
        """
        pass

