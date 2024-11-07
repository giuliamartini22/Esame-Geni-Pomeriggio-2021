import networkx as nx
from database.DAO import DAO
class Model:
    def __init__(self):
        self._nodes = []
        self._edges = []
        self.graph = nx.Graph()
        self._listLocalizations = []
        self._listConnectedLocalizations = []
        self._listGenes = []
        self.listTuple = []
        self.listaCoppie = []

    def getLocalization(self):
        self._listLocalizations = DAO.getAllLocalization()
        return self._listLocalizations

    def build_graph(self):
        self._nodes = DAO.getAllLocalization()
        self.graph.add_nodes_from(self._nodes)
        self._listConnectedLocalizations = DAO.getAllConnectedLocalizations()

        for e in self._listConnectedLocalizations:
            if e[0] in self._nodes and e[1] in self._nodes:
                if self.graph.has_edge(e[0], e[1]):
                    self.graph[e[0]][e[1]]['weight'] += 1
                else:
                    self.graph.add_edge(e[0], e[1], weight=e[2])

    def calcolaAdiacenti(self, l):
        listaAdiacenti = []
        if l in self._nodes:
            for edge in self.graph.neighbors(l):
                peso = self.graph[l][edge]["weight"]
                listaAdiacenti.append((edge, peso))
        listaAdiacenti.sort(key=lambda x: x[1], reverse=True)
        return listaAdiacenti

    def get_nodes(self):
        return self.graph.nodes()

    def get_edges(self):
        return list(self.graph.edges(data=True))

    def get_num_of_nodes(self):
        return self.graph.number_of_nodes()

    def get_num_of_edges(self):
        return self.graph.number_of_edges()