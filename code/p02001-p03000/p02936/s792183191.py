#!/usr/bin/env python3
import sys
from collections import deque
INF = float("inf")


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.E = [[] for _ in range(N)]

    def add_edge(self, edge):
        """辺を加える。edgeは(始点, 終点、重み)からなるリスト
        重みがなければ、重み1とする。
        """
        if len(edge) == 2:
            edge.append(1)
        elif len(edge) != 3:
            print("error in add_edge")

        s, t, w = edge
        self.E[s].append([t, w])
        self.E[t].append([s, w])


def solve(N: int, Q: int, a: "List[int]", b: "List[int]", p: "List[int]", x: "List[int]"):
    g = Graph(N)
    for aa, bb in zip(a, b):
        g.add_edge([aa-1, bb-1, 1])

    P = [0]*N
    for pp, xx in zip(p, x):
        P[pp-1] += xx

    visit = deque()
    visit.append((0, None))
    counter = [0]*N
    while len(visit) > 0:
        # print(visit)
        curr, par = visit.popleft()
        counter[curr] += P[curr]
        for t, w in g.E[curr]:
            if t == par:
                continue
            visit.append((t, curr))
            counter[t] += counter[curr]
    print(*counter)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    a = [int()] * (N-1)  # type: "List[int]"
    b = [int()] * (N-1)  # type: "List[int]"
    for i in range(N-1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    p = [int()] * (Q)  # type: "List[int]"
    x = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        p[i] = int(next(tokens))
        x[i] = int(next(tokens))
    solve(N, Q, a, b, p, x)


if __name__ == '__main__':
    main()
