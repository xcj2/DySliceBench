class DirectedEdge(object):
    def __init__(self, v, w, weight, id):
        self.v = v
        self.w = w
        self.weight = weight
        self.id = id

    def __str__(self):
        return "[{} -> {}: {}]".format(self.v, self.w, self.weight)

    def edge_from(self):
        return self.v

    def edge_to(self):
        return self.w

    def get_weight(self):
        return self.weight

    def get_id(self):
        return self.id



class EdgeWeightedDigraph(object):
    def __init__(self, vertex_size):
        self.VERTEX_SIZE = vertex_size
        self.adj = [set() for x in range(self.get_vertex_size())]

    def get_vertex_size(self):
        return self.VERTEX_SIZE

    def add_edge(self, edge):
        v = edge.edge_from()
        self.adj[v].add(edge)

    def get_adj(self, v):
        res = set()
        for edge in self.adj[v]:
            res.add(edge)
        return res


class IndexMinPQ(object):
    def __init__(self, size):
        self.keys = [None for x in range(size + 1)]  # key を格納
        self.pq = [None for x in range(size + 1)]    # tree 構造を形成する. key の id を格納

        self.qp = [None for x in range(size + 1)]

        self.n = 0

    def contains(self, i):
        if self.qp[i] is None:
            return False
        else:
            return True

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def decrease_key(self, i, key):
        self.keys[i] = key
        self._swim(self.qp[i])

    def insert(self, i, key):
        tail = self.n + 1
        self.pq[tail] = i
        self.qp[i] = tail
        self.keys[i] = key

        self._swim(tail)

        self.n += 1

    def _swim(self, i):
        while i != 1:
            p = self._get_parent_pos(i)
            if not self._is_less(p, i):
                self._exch(p, i)
                i = p
            else:
                break

    def del_min(self):
        head = self.pq[1]

        self.pq[1] = None
        self.keys[head] = None
        self.qp[head] = None

        self._exch(1, self.n)

        self.n -= 1
        self._sink(1)

        return head

    def _sink(self, i):
        while self._get_left_child_pos(i) <= self.n:
            left = self._get_left_child_pos(i)
            right = left + 1

            child = left
            if not left == self.n and not self._is_less(left, right):
                child = right

            if not self._is_less(i, child):
                self._exch(i, child)
                i = child
            else:
                break

    def _is_less(self, a, b):
        a_id = self.pq[a]
        b_id = self.pq[b]
        return self.keys[a_id] < self.keys[b_id]

    def _get_parent_pos(self, i):
        return i // 2

    def _get_left_child_pos(self, i):
        return i * 2

    def _exch(self, a, b):
        swap = self.pq[a]
        self.pq[a] = self.pq[b]
        self.pq[b] = swap

        if self.pq[a] is not None:
            self.qp[self.pq[a]] = a
        if self.pq[b] is not None:
            self.qp[self.pq[b]] = b


class DijkstraShortestPath(object):
    def __init__(self, edge_weighted_digraph, source):
        self.digraph = edge_weighted_digraph
        self.source = source

        self.edge_to = [None for x in range(self.digraph.get_vertex_size())]
        self.dist_to = [float("infinity") for x in range(self.digraph.get_vertex_size())]
        self.ipq = IndexMinPQ(self.digraph.get_vertex_size())

        self.dist_to[source] = 0.0
        self.ipq.insert(source, self.dist_to[source])

        while not self.ipq.is_empty():
            v = self.ipq.del_min()
            for edge in self.digraph.get_adj(v):
                self._relax(edge)

    def _relax(self, edge):
        v = edge.edge_from()
        w = edge.edge_to()
        if self.dist_to[v] + edge.get_weight() < self.dist_to[w]:
            self.dist_to[w] = self.dist_to[v] + edge.get_weight()
            self.edge_to[w] = edge

            if self.ipq.contains(w):
                self.ipq.decrease_key(w, self.dist_to[w])
            else:
                self.ipq.insert(w, self.dist_to[w])

    def has_path_to(self, v):
        return self.dist_to[v] < float("infinity")

    def path_to(self, v):
        path = []
        while self.edge_to[v] is not None:
            edge = self.edge_to[v]
            path.append(edge)
            v = edge.edge_from()
        return path


def solve():
    N, M = map(int, input().split())
    ABC = []
    for _ in range(M):
        ABC.append(tuple(map(int, input().split())))

    edges = []
    G = EdgeWeightedDigraph(N + 1)
    for a, b, c in ABC:
        edge_a = DirectedEdge(int(a), int(b), float(c), (a, b))
        edge_b = DirectedEdge(int(b), int(a), float(c), (a, b))

        G.add_edge(edge_a)
        G.add_edge(edge_b)

        edges.append((a, b))

    founds = set()
    for s in range(1, N + 1):
        sp = DijkstraShortestPath(G, s)
        for v in range(1, N + 1):
            if not v == s:
                for e in sp.path_to(v):
                    # print(s, v, e)
                    founds.add(e.get_id())

    ans = len(edges) - len(founds)

    return ans


if __name__ == '__main__':
    res = solve()
    print(res)
