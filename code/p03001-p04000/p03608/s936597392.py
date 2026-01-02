import itertools


class Graph:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.edges = [[] for _ in range(n_nodes)]

    def add_edge(self, s, t, d=None, undirected=False):
        if d is not None:
            self.edges[s].append((t, d))
        else:
            self.edges[s].append(t)
        if undirected:
            self.add_edge(t, s, d)

    def add_edges(self, edges, undirected=False):
        for edge in edges:
            self.add_edge(*edge, undirected=undirected)


class FloydWarshall:
    def __init__(self, graph):
        self.graph = graph
        self.distances = [[float('inf')] * graph.n_nodes
                          for _ in range(graph.n_nodes)]
        self.nexts = [[None] * graph.n_nodes for _ in range(graph.n_nodes)]
        self._init()

    def _init(self):
        for x in range(self.graph.n_nodes):
            self.distances[x][x] = 0
        for source in range(self.graph.n_nodes):
            for destination, distance in self.graph.edges[source]:
                self.distances[source][destination] = distance
                self.nexts[source][destination] = destination

    def compute_shortest_path_lengths(self):
        for k in range(self.graph.n_nodes):
            for i in range(self.graph.n_nodes):
                for j in range(self.graph.n_nodes):
                    s = self.distances[i][k] + self.distances[k][j]
                    if s < self.distances[i][j]:
                        self.distances[i][j] = s
                        self.nexts[i][j] = self.nexts[i][k]

    def get_shortest_path(self, x, y):
        if self.nexts[x][y] is None:
            return []
        path = [x]
        while path[-1] != y:
            s = path[-1]
            t = self.nexts[s][y]
            path.append(t)
        return path


n, m, r = map(int, input().split())
rs = list(map(int, input().split()))

graph = Graph(n + 1)
graph.add_edges([list(map(int,
                          input().split())) for _ in range(m)],
                undirected=True)
fw = FloydWarshall(graph)
fw.compute_shortest_path_lengths()
res = float('inf')
for perm in itertools.permutations(rs):
    s = sum([fw.distances[a][b] for a, b in zip(perm, perm[1:])])
    res = min(res, s)
print(res)