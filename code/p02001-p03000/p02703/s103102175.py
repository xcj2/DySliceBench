#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")
from collections import defaultdict
from collections import deque
import heapq


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.E = defaultdict(list)

    def add_edge(self, s, t, w=1):
        self.E[s].append((t, w))
        # self.E[t].append((s, w))


def shortestPath(g: Graph, s: int):
    # 返り値 (dist, prev)
    # dist: 始点からの距離が格納されたリスト
    # prev: 始点から最短経路で移動する場合、各頂点に至る前の頂点のリスト
    dist = defaultdict(lambda: INF)
    dist[s] = 0

    prev = defaultdict(lambda: None)
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


def solve(N: int, M: int, S: int,
          U: "List[int]", V: "List[int]",
          A: "List[int]", B: "List[int]",
          C: "List[int]", D: "List[int]"):

    # (頂点数, 所持している銀貨の枚数)ごとにノードを増やす
    # ノード数は 50*(N-1)*N 未満
    NN = 50*N*N
    g = Graph(NN)
    # U[i]-1, V[i]-1間ではなくて、
    # (U[i]-1, a), (V[i]-1, a-A[i])間に重みB[i]の有向リンクがある
    # (V[i]-1, a), (U[i]-1, a-A[i])間に重みB[i]の有向リンクがある
    for i in range(M):
        for j in range(50*N):
            if j - A[i] < 0:
                continue
            g.add_edge((U[i]-1, j), (V[i]-1, j-A[i]), B[i])
            g.add_edge((V[i]-1, j), (U[i]-1, j-A[i]), B[i])
        # print(U[i]-1, V[i]-1)
    # 都市iで補給する時のパス
    for i in range(N):
        for j in range(50*N):
            if j-C[i] >= 0:
                g.add_edge((i, j-C[i]), (i, j), D[i])

    if S >= (N-1)*50:
        S = (N-1)*50
    dist, prev = shortestPath(g, (0, S))
    # print(dist, prev)

    # nに至るパスで最短時間となるものを選ぶ
    for n in range(1, N):
        tot = INF
        for i in range(50*N):
            if (n, i) in dist:
                tot = min(tot, dist[n, i])
                # print((n, i), dist[n, i], prev[n, i])
        print(tot)
        # print(n, "done")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    U = [int()] * (M)  # type: "List[int]"
    V = [int()] * (M)  # type: "List[int]"
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        U[i] = int(next(tokens))
        V[i] = int(next(tokens))
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    C = [int()] * (N)  # type: "List[int]"
    D = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, M, S, U, V, A, B, C, D)


if __name__ == '__main__':
    main()
