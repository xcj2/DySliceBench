#!/usr/bin/env python3
import sys
import heapq
from collections import Counter
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


def solve(H: int, W: int, c: "List[List[int]]", A: "List[List[int]]"):
    g = Graph(10)
    # 向きを逆向きにuとｒ
    for i in range(10):
        for j in range(10):
            g.add_edge([j, i, c[i][j]])

    c = Counter()
    for a in A:
        c.update(a)

    # 逆向きにとった効果として、１から他の数字への距離を求めれば良い
    dist, prev = shortestPath(g, 1)
    # print(dist)
    # print(c)
    ans = 0
    for key in c:
        if key == 1 or key == -1:
            continue
        ans += dist[key]*c[key]

    print(ans)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    c = [[int(next(tokens)) for _ in range(9-0+1)]
         for _ in range(9-0+1)]  # type: "List[List[int]]"
    A = [[int(next(tokens)) for _ in range(W)]
         for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, c, A)


if __name__ == '__main__':
    main()
