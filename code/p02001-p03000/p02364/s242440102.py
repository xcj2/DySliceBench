# GRL_2_A: Minimum Spanning Tree

from collections import namedtuple
from heapq import heappop, heappush


class UnionFind:
    def __init__(self, n):
        self.nodes = [i for i in range(n)]
        self.sizes = [1 for _ in range(n)]

    def union(self, p, q):
        rp = self.root(p)
        rq = self.root(q)
        if self.sizes[rp] > self.sizes[rq]:
            self.nodes[rq] = rp
            self.sizes[rp] += self.sizes[rq]
        else:
            self.nodes[rp] = rq
            self.sizes[rq] += self.sizes[rp]

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def root(self, p):
        while p != self.nodes[p]:
            self.nodes[p] = self.nodes[self.nodes[p]]
            p = self.nodes[p]

        return p


WEIGHT_MAX = 10 ** 10
WeightedEdge = namedtuple('WeightedEdge', ('src', 'dest', 'weight'))


class Digraph:
    def __init__(self, v):
        self.v = v
        self._edges = [[] for _ in range(v)]

    def add(self, edge):
        self._edges[edge.src].append(edge)

    def adj(self, v):
        return self._edges[v]

    def edges(self):
        for es in self._edges:
            for e in es:
                yield e


def mst_kruskal(graph):
    edges = []
    for e in graph.edges():
        heappush(edges, (e.weight, e))

    uf = UnionFind(graph.v)
    conn = 0
    weight = 0
    while conn < graph.v-1:
        w, e = heappop(edges)
        if not uf.connected(e.src, e.dest):
            uf.union(e.src, e.dest)
            conn += 1
            weight += w

    return weight


def run():
    v, e = [int(i) for i in input().split()]
    graph = Digraph(v)

    for _ in range(e):
        s, t, w = [int(i) for i in input().split()]
        graph.add(WeightedEdge(s, t, w))

    print(mst_kruskal(graph))


if __name__ == '__main__':
    run()

