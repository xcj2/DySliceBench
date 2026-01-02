# Edige Weighted Digraph


from collections import namedtuple


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


def mca_chu_liu_edmonds(graph, s):
    def select_edges():
        es = [None] * graph.v
        for v in range(graph.v):
            for e in graph.adj(v):
                w = e.dest
                if w == s:
                    continue
                if es[w] is None or e.weight < es[w].weight:
                    es[w] = e
        return es

    def find_cycle(es):
        vs = [0 for _ in range(graph.v)]
        for e in es:
            if e is None:
                continue
            vs[e.src] += 1
        leaves = [v for v, c in enumerate(vs) if c == 0]
        while leaves:
            leaf, *leaves = leaves
            if es[leaf] is not None:
                w = es[leaf].src
                vs[w] -= 1
                if vs[w] == 0:
                    leaves.append(w)
        cycle = []
        for v, c in enumerate(vs):
            if c > 0:
                cycle.append(v)
                u = es[v].src
                while u != v:
                    cycle.append(u)
                    u = es[u].src
                break
        return cycle

    def contract(es, vs):
        vvs = []
        vv = 0
        c = graph.v - len(vs)
        for v in range(graph.v):
            if v in vs:
                vvs.append(c)
            else:
                vvs.append(vv)
                vv += 1
        g = Digraph(c+1)
        for v in range(graph.v):
            for e in graph.adj(v):
                if e.src not in vs or e.dest not in vs:
                    v = vvs[e.src]
                    w = vvs[e.dest]
                    weight = e.weight
                    if e.dest in vs:
                        weight -= es[e.dest].weight
                    e = WeightedEdge(v, w, weight)
                    g.add(e)
        return g, vvs[s]

    edges = select_edges()
    cycle = find_cycle(edges)

    if cycle:
        g, ss = contract(edges, cycle)
        return mca_chu_liu_edmonds(g, ss) + sum(edges[v].weight for v in cycle)
    else:
        return sum(e.weight for e in edges if e is not None)


def run():
    v, e, r = [int(i) for i in input().split()]
    graph = Digraph(v)

    for _ in range(e):
        s, t, w = [int(i) for i in input().split()]
        graph.add(WeightedEdge(s, t, w))

    print(mca_chu_liu_edmonds(graph, r))


if __name__ == '__main__':
    run()

