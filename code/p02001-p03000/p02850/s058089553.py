#!/usr/bin/env python3
import sys
from collections import deque
from collections import defaultdict
INF = float("inf")


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.E = defaultdict(list)

    def add_edge(self, src, dest, w=1):
        self.E[src].append((dest, w))
        self.E[dest].append((src, w))


def solve(N: int, a: "List[int]", b: "List[int]"):

    g = Graph(N)
    for i, (aa, bb) in enumerate(zip(a, b)):
        g.add_edge(aa-1, bb-1, i)

    visited = [False]*N
    edge_color = [-1]*(N-1)

    q = deque([(0, -1)])

    while len(q) > 0:
        node, color = q.popleft()
        penki = 1
        if color == penki:
            penki += 1

        for to_, weight in g.E[node]:
            if edge_color[weight] != -1:
                continue
            edge_color[weight] = penki
            q.append((to_, penki))
            penki += 1
            if color == penki:
                penki += 1

    print(max([len(g.E[k]) for k in g.E]))
    print(*edge_color, sep="\n")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, a, b)


if __name__ == '__main__':
    main()
