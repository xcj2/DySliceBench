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
            if dist[v] > dist[u]+w:
                dist[v] = dist[u]+w
                prev[v] = u
                heapq.heappush(Q, (dist[v], v))
    return dist, prev


def solve(N: int, M: int, u: "List[int]", v: "List[int]", S: int, T: int):
    g1 = Graph(3*N)
    for from_, to_ in zip(u, v):
        g1.add_edge((from_-1, N+to_-1, 1))
        g1.add_edge((N+from_-1, 2*N+to_-1, 1))
        g1.add_edge((2*N+from_-1, to_-1, 1))

    dist1, prev1 = shortestPath(g1, S-1)
    # print(dist1)
    # print(dist1)
    m = INF
    for i in range(3):
        if dist1[i*N+T-1] % 3 == 0 and m > (dist1[i*N+T-1]//3):
            m = dist1[i*N+T-1]//3
    if m == INF:
        print(-1)
    else:
        print(m)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    u = [int()] * (M)  # type: "List[int]"
    v = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    S = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    solve(N, M, u, v, S, T)


if __name__ == '__main__':
    main()
