
from collections import namedtuple
from heapq import heappop, heappush


WEIGHT_MAX = 10 ** 10
WeightedEdge = namedtuple('WeightedEdge', ('src', 'dest', 'weight'))


class Digraph:
    def __init__(self, v):
        self.v = v
        self.edges = [[] for _ in range(v)]

    def add(self, edge):
        self.edges[edge.src].append(edge)

    def adj(self, v):
        return self.edges[v]


def sp_dijkstra(graph, s):
    def push_node(v):
        if v in index:
            index[v][2] = False
        node = [dists[v], v, True]
        heappush(nodes, node)
        index[v] = node

    def pop_node():
        while nodes:
            node = heappop(nodes)
            if node[2]:
                return node[1]
        return None

    def relax(edge):
        s, t, w = edge
        if dists[t] > dists[s] + w:
            dists[t] = dists[s] + w
            srcs[t] = s
            push_node(t)

    nodes = []
    index = {}
    dists = [WEIGHT_MAX] * graph.v
    dists[s] = 0
    srcs = [-1] * graph.v

    v = s
    while v is not None:
        for e in graph.adj(v):
            relax(e)
        v = pop_node()

    return [None if dists[v] == WEIGHT_MAX else dists[v]
            for v in range(graph.v)]


def run():
    v, e, r = [int(i) for i in input().split()]

    digraph = Digraph(v)
    for _ in range(e):
        edge = WeightedEdge(*[int(i) for i in input().split()])
        digraph.add(edge)

    for w in sp_dijkstra(digraph, r):
        if w is None:
            print('INF')
        else:
            print(w)


if __name__ == '__main__':
    run()

