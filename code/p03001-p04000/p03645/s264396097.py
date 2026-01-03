#!/usr/bin/env python3
import sys
INF = float("inf")


def yes():
    print("POSSIBLE")  # type: str


def no():
    print("IMPOSSIBLE")  # type: str


import heapq
INF = float("inf")


# 無向グラフを仮定する。
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
            print("error in add_edge")
            pass

        s, t, w = edge
        self.E[s].append([t, w])
        self.E[t].append([s, w])  # 無向グラフを仮定。逆向きにも辺を張る

        pass


def shortestPath(g: Graph, s: int):
    """ グラフgにおいて、始点sから各頂点への最短路を求める
    引数
    g: グラフ, s: 始点
    返り値
    dist: 始点からの距離が格納されたリスト
    prev: 始点から最短経路で移動する場合、各頂点に至る前の頂点のリスト
    """
    dist = [INF]*g.N
    dist[s] = 0

    prev = [None]*g.N
    Q = []
    heapq.heappush(Q, (dist[s], s))

    while len(Q) > 0:
        _, u = heapq.heappop(Q)
        for v, w in g.E[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(Q, (dist[v], v))
    return dist, prev


def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    g = Graph(N)
    for aa, bb in zip(a, b):
        g.add_edge([aa-1, bb-1, 1])

    dist, prev = shortestPath(g, 0)
    if dist[N-1] <= 2:
        yes()
    else:
        no()
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
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, M, a, b)


if __name__ == '__main__':
    main()
