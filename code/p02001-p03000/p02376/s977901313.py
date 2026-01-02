from heapq import heappush, heappop


class Edge:
    __slots__ = ('src', 'dest', 'capacity', 'flow')

    def __init__(self, v, w, capacity):
        self.src = v
        self.dest = w
        self.capacity = capacity
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

    def add_flow(self, v, f):
        if v == self.src:
            self.flow += f
        else:
            self.flow -= f


class Network:
    def __init__(self, v):
        self.v = v
        self._edges = [[] for _ in range(v)]

    def add(self, edge):
        self._edges[edge.src].append(edge)
        self._edges[edge.dest].append(edge)

    def adj(self, v):
        return self._edges[v]


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

    return sum(e.flow for e in network.adj(s) if e.src == s)


def run():
    v, e = [int(i) for i in input().split()]
    s, t = 0, v-1
    net = Network(v)

    for _ in range(e):
        v, w, c = [int(i) for i in input().split()]
        net.add(Edge(v, w, c))

    print(max_flow(net, s, t))


if __name__ == '__main__':
    run()

