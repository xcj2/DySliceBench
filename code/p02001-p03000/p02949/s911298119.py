#!/usr/bin/env python3
import sys
from collections import deque
INF = float("inf")


# 有効グラフを仮定する。
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


def BellmanFord(g: Graph, s):
    """ベルマンフォード法による最短経路
    """
    N = g.N
    dist = [INF]*N
    dist[s] = 0
    prev = [None]*N

    # 辺の緩和
    for _ in range(N):
        for from_ in range(N):      # ここの２重ループはO(M)
            for to_, weight in g.E[from_]:
                if dist[to_] > dist[from_] + weight:
                    dist[to_] = dist[from_] + weight
                    prev[to_] = from_
    # 負の重みの閉路がないかチェック
    for from_ in range(N):
        for to_, weight in g.E[from_]:
            if dist[from_]+weight < dist[to_]:
                return None, None

    return dist, prev


def solve(N: int, M: int, P: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    for i in range(M):
        C[i] = P - C[i]

    rev_g = Graph(N)
    for a, b, c in zip(A, B, C):
        rev_g.add_edge([b-1, a-1, c])

    # Nに到達できないノードは除く
    visitable = [False]*N
    visitable[N-1] = True
    q = deque()
    q.append(N-1)
    while len(q) > 0:
        curr = q.popleft()
        for t_, w in rev_g.E[curr]:
            if not visitable[t_]:
                visitable[t_] = True
                q.append(t_)

    g = Graph(N)
    for a, b, c in zip(A, B, C):
        if visitable[a-1] and visitable[b-1]:
            g.add_edge([a-1, b-1, c])

    dist, prev = BellmanFord(g, 0)
    if dist is None:
        print(-1)
    else:
        print(max(-dist[-1], 0))

    # print(longest)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, P, A, B, C)


if __name__ == '__main__':
    main()
