#!/usr/bin/env python3
import sys
INF = float("inf")


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.V = list(range(N))
        self.E = [[] for _ in range(N)]

    def add_edge(self, edge):
        """辺を加える。edgeは(始点, 終点、重み)からなるリスト
        重みがなければ、重み1とする。
        """
        if len(edge) == 2:
            edge.append(1)
        elif len(edge) != 3:
            return None

        s, t, w = edge
        self.E[s].append([t, w])
        return True


def BellmanFord(g: Graph, s):
    """ベルマンフォード法によって最短経路を求める
    """
    N = g.N
    dist = [INF]*N
    dist[s] = 0
    prev = [None]*N

    # 辺の緩和
    for i in range(N):
        for from_ in range(N):      # ここの２重ループはO(M)
            for to_, weight in g.E[from_]:
                if dist[to_] > dist[from_] + weight:
                    dist[to_] = dist[from_] + weight
                    prev[to_] = from_
                    if i == N-1 and to_ == N-1:
                        return None, None

    return dist, prev


def solve(N: int, M: int, a: "List[int]", b: "List[int]", c: "List[int]"):
    g = Graph(N)
    for f, t, w in zip(a, b, c):
        g.add_edge([f-1, t-1, -w])

    dist, prev = BellmanFord(g, 0)

    if dist == None:
        print("inf")
    else:
        print(-dist[N-1])

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    c = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, M, a, b, c)


if __name__ == '__main__':
    main()
