#!/usr/bin/env python3
# GRL_7_A: Matching - Bipertite Matching


from heapq import heappush, heappop


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


def max_flow(network, s, t):
    def augment_path():
        marked = [False] * network.v
        edge_to = [None] * network.v
        n = 0
        heap = [(-10**6, s, n, None)]
        while heap:
            cap, v, _, e = heappop(heap)
            edge_to[v] = e
            if v == t:
                return (-cap, edge_to)
            if not marked[v]:
                marked[v] = True
                for ne in network.adj(v):
                    n += 1
                    w = ne.other(v)
                    c = ne.residual_capacity(v)
                    if not marked[w] and c > 0:
                        heappush(heap, (max(-c, cap), w, n, ne))

        return (0, [])

    while True:
        cap, path = augment_path()
        if cap == 0:
            break
        v = t
        e = path[t]
        while e is not None:
            v = e.other(v)
            e.add_flow(v, cap)
            e = path[v]

    return network.flow(s)


def run():
    n, m, e = [int(i) for i in input().split()]
    s, t = 0, n+m+1
    net = Network(n+m+2)
    for i in range(n):
        net.add(Edge(s, i+1, 1))
    for j in range(m):
        net.add(Edge(j+1+n, t, 1))

    for _ in range(e):
        x, y = [int(i) for i in input().split()]
        edge = Edge(x+1, y+1+n, 1)
        net.add(edge)

    print(max_flow(net, s, t))


if __name__ == '__main__':
    run()

