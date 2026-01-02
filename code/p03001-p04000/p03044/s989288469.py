#!/usr/bin/env python3
import sys
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


def solve(N: int, u: "List[int]", v: "List[int]", w: "List[int]"):

    g = Graph(N)
    for _u, _v, _w in zip(u, v, w):
        g.add_edge([_u-1, _v-1, _w])  # インデックスのとり方が違うので調整。

    dist, prev = shortestPath(g, 0)

    for d in dist:
        if d % 2 == 0:
            print(0)
        else:
            print(1)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    u = [int()] * (N-1)  # type: "List[int]"
    v = [int()] * (N-1)  # type: "List[int]"
    w = [int()] * (N-1)  # type: "List[int]"
    for i in range(N-1):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
        w[i] = int(next(tokens))
    solve(N, u, v, w)


if __name__ == '__main__':
    main()
