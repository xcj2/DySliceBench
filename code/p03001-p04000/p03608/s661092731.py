#!/usr/bin/env python3
import sys
from itertools import permutations
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
            print("error in add_edge")
            pass

        s, t, w = edge
        self.E[s].append([t, w])
        self.E[t].append([s, w])  # 無向グラフを仮定。逆向きにも辺を張る

        pass


def Warshall_Floyd(g: Graph):
    """ワーシャルフロイド法により、全節点対の最短距離を求める。O(V^3)
    https://ja.wikipedia.org/wiki/%E3%83%AF%E3%83%BC%E3%82%B7%E3%83%A3%E3%83%AB%E2%80%93%E3%83%95%E3%83%AD%E3%82%A4%E3%83%89%E6%B3%95
    """
    N = g.N
    dist = [[INF]*N for _ in range(N)]
    for from_, toweights in enumerate(g.E):
        for to_, w in toweights:
            dist[from_][to_] = w

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


def solve(N: int, M: int, R: int, r: "List[int]", A: "List[int]", B: "List[int]", C: "List[int]"):

    g = Graph(N)
    for a, b, c in zip(A, B, C):
        g.add_edge([a-1, b-1, c])

    B = Warshall_Floyd(g)

    m = INF
    for order in permutations(r, R):
        counter = 0
        for i in range(R-1):
            counter += B[order[i]-1][order[i+1]-1]
        m = min(m, counter)
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
    R = int(next(tokens))  # type: int
    r = [int(next(tokens)) for _ in range(R)]  # type: "List[int]"
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, R, r, A, B, C)


if __name__ == '__main__':
    main()
