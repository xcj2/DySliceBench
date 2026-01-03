#!/usr/bin/env python3
import sys
import heapq
INF = float("inf")


class Graph(object):

    def __init__(self, N):
        self.N = N
        self.E = []

    def add_edge(self, edge):
        """
        args:
          edge : (from_, to_, weight)
        """
        s, t, w = edge
        if s > t:
            s, t = t, s
        self.E.append([s, t, w])


class UnionFind(object):
    """UnionFind木
    """

    def __init__(self, N):
        self.tree = list(range(N))

    def root(self, i):
        if self.tree[i] == i:
            return i
        else:
            self.tree[i] = self.root(self.tree[i])
            return self.tree[i]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            self.tree[x] = y


def solve(N: int, x: "List[int]", y: "List[int]"):

    XYN = sorted(zip(x, y, range(N)))
    YXN = sorted(zip(y, x, range(N)))
    edges = []
    for i in range(N-1):
        (x1, y1, n1), (x2, y2, n2) = XYN[i:i+2]
        heapq.heappush(edges, [min(abs(x1-x2), abs(y1-y2)), n1, n2])
        (y1, x1, n1), (y2, x2, n2) = YXN[i:i+2]
        heapq.heappush(edges, [min(abs(x1-x2), abs(y1-y2)), n1, n2])
    tot, counter = 0, 0
    group = UnionFind(N)
    while len(edges) > 0 and counter <= N:
        w, f, t = heapq.heappop(edges)
        if not group.same(f, t):
            tot += w
            counter += 1
            group.unite(f, t)

    print(tot)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, x, y)


if __name__ == '__main__':
    main()
