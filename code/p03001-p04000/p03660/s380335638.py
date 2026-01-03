#!/usr/bin/env python3
import sys
import math
from collections import defaultdict, deque
import heapq

INF = float("inf")


class Graph(object):
    """グラフを扱うオブジェクト
    """

    def __init__(self, N):
        self.N = N
        self.edges = defaultdict(list)
        pass

    def add_edge(self, from_, to_, weight=1):
        """必ず0インデックスで入力すること。
        """
        self.edges[from_].append([to_, weight])
        self.edges[to_].append([from_, weight])

    def remove_edge(self, from_, to_):
        for t_, w_ in self.edges[from_]:
            if t_ == to_:
                break
        self.edges[from_].remove([t_, w_])
        self.edges[t_].remove([from_, w_])


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
        for v, w in g.edges[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(Q, (dist[v], v))
    return dist, prev


class UnionFind(object):
    """UnionFind木
    """

    def __init__(self, N):
        self.tree = list(range(N))

    def root(self, i):
        if self.tree[i] == i:
            return i
        else:
            self.tree[i] = self.root(self.tree[i])
            return self.tree[i]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            self.tree[x] = y


def solve(N: int, a: "List[int]", b: "List[int]"):
    g = Graph(N)
    for x, y in zip(a, b):
        g.add_edge(x-1, y-1, 1)

    dist, prev = shortestPath(g, 0)

    depth = dist[N-1]
    boundary = N-1
    for _ in range((depth-1) // 2):
        boundary = prev[boundary]
    g.remove_edge(boundary, prev[boundary])
    # print(boundary, prev[boundary])

    visited = [False]*N
    countA = 0
    q = deque()
    q.append(0)
    while len(q) > 0:
        curr = q.popleft()
        visited[curr] = True
        countA += 1
        for t_, w_ in g.edges[curr]:
            if visited[t_] == False:
                q.append(t_)
    countB = N-countA
    if countA > countB:
        print("Fennec")
    else:
        print("Snuke")
    # print(countA, countB)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N-1)  # type: "List[int]"
    b = [int()] * (N-1)  # type: "List[int]"
    for i in range(N-1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, a, b)


if __name__ == '__main__':
    main()
