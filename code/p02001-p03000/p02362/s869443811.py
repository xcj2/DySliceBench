# Edige Weighted Digraph


from collections import namedtuple


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


def sp_bellmanford(graph, s):
    def relax(edge):
        s, t, w = edge
        if dists[t] > dists[s] + w:
            dists[t] = dists[s] + w
            srcs[t] = s
            _nodes.append(t)

    dists = [WEIGHT_MAX] * graph.v
    dists[s] = 0
    srcs = [-1] * graph.v
    nodes = []

    nodes.append(s)
    for _ in range(graph.v):
        _nodes = []
        for v in nodes:
            for e in graph.adj(v):
                relax(e)
        nodes = _nodes

    if len(nodes) > 0:
        return None
    else:
        return [None if dists[v] == WEIGHT_MAX else dists[v]
                for v in range(graph.v)]


def run():
    v, e, r = [int(i) for i in input().split()]

    graph = Digraph(v)
    for _ in range(e):
        edge = WeightedEdge(*[int(i) for i in input().split()])
        graph.add(edge)

    ws = sp_bellmanford(graph, r)
    if ws is None:
        print("NEGATIVE CYCLE")
    else:
        for w in ws:
            if w is None:
                print("INF")
            else:
                print("{:d}".format(w))


if __name__ == '__main__':
    run()

