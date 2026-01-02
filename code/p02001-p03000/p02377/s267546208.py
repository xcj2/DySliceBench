#!/usr/bin/env python3
# GRL_6_B: Minimum Cost Flow


WEIGHT_MAX = 10 ** 10


class Edge:
    __slots__ = ('src', 'dest', 'capacity', 'flow', 'cost')

    def __init__(self, v, w, capacity, cost=0):
        self.src = v
        self.dest = w
        self.capacity = capacity
        self.cost = cost
        self.flow = 0

    def other(self, v):
        if v == self.src:
            return self.dest
        else:
            return self.src

    def residual_capacity(self, v):
        if v == self.src:
            return self.capacity - self.flow
        else:
            return self.flow

    def cost_from(self, v):
        if v == self.src:
            return self.cost
        else:
            return -self.cost

    def add_flow(self, v, f):
        if v == self.src:
            self.flow += f
        else:
            self.flow -= f

    def __str__(self):
        return "{} {} {} {} {}".format(self.src, self.dest, self.capacity,
                                       self.cost, self.flow)


class Network:
    def __init__(self, v):
        self.v = v
        self._edges = [[] for _ in range(v)]

    def add(self, edge):
        self._edges[edge.src].append(edge)
        self._edges[edge.dest].append(edge)

    def adj(self, v):
        return self._edges[v]

    def flow(self, v):
        return sum(e.flow for e in self.adj(v) if e.src == v)

    def cost(self):
        cost = 0
        for v in range(self.v):
            for e in self.adj(v):
                if e.src == v:
                    cost += e.flow * e.cost
        return cost

    def __str__(self):
        s = ''
        for v in range(self.v):
            for e in self.adj(v):
                s += "{} {}\n".format(v, e)

        return s


def min_cost(network, s, t, f):
    def augment_path():
        def relax(edge, v):
            w = edge.other(v)
            c = edge.cost_from(v)
            if e.residual_capacity(v) > 0 and dists[w] > dists[v] + c:
                dists[w] = dists[v] + c
                edge_to[w] = e
                _nodes.append(w)

        dists = [WEIGHT_MAX] * network.v
        dists[s] = 0
        edge_to = [None] * network.v
        nodes = []

        nodes.append(s)
        for _ in range(network.v):
            _nodes = []
            for v in nodes:
                for e in network.adj(v):
                    relax(e, v)
            nodes = _nodes

        if edge_to[t] is None:
            return (0, [])
        else:
            v = t
            e = edge_to[v]
            cap = f
            while e is not None:
                v = e.other(v)
                _cap = e.residual_capacity(v)
                if cap > _cap:
                    cap = _cap
                e = edge_to[v]
            return (cap, edge_to)

    while f > 0:
        cap, path = augment_path()
        if cap == 0:
            break
        f -= cap
        v = t
        e = path[t]
        while e is not None:
            v = e.other(v)
            e.add_flow(v, cap)
            e = path[v]

    if f > 0:
        return -1
    else:
        return network.cost()


def run():
    v, e, f = [int(i) for i in input().split()]
    net = Network(v)
    s, t = 0, v-1

    for _ in range(e):
        v, w, c, d = [int(i) for i in input().split()]
        net.add(Edge(v, w, c, d))

    print(min_cost(net, s, t, f))


if __name__ == '__main__':
    run()

