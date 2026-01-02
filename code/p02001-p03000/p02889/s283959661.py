import sys

input = sys.stdin.readline


def read_i():
    return list(map(int, input().split()))


def read_is(n=1):
    return [read_i() for _ in range(n)]


class Graph:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.edges = [[float('inf')] * n_nodes for _ in range(n_nodes)]

    def add_edge(self, s, t, d=None, undirected=False):
        if d is None:
            d = 1
        self.edges[s][t] = d
        if undirected:
            self.edges[t][s] = d


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
            for destination, distance in enumerate(self.graph.edges[source]):
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


n, m, l = read_i()
graph = Graph(n)
for _ in range(m):
    a, b, c = read_i()
    if c > l:
        continue
    graph.add_edge(a - 1, b - 1, d=c, undirected=True)
fw = FloydWarshall(graph)
fw.compute_shortest_path_lengths()

graph2 = Graph(n)
for s in range(n):
    for t in range(n):
        if s >= t:
            continue
        if fw.distances[s][t] > l:
            continue
        graph2.add_edge(s, t, d=1, undirected=True)
fw = FloydWarshall(graph2)
fw.compute_shortest_path_lengths()

q = int(input())
for _ in range(q):
    s, t = read_i()
    s -= 1
    t -= 1
    d = fw.distances[s][t] - 1
    if d == float('inf'):
        print(-1)
    else:
        print(d)