#!/usr/bin/env python3
import sys
import math
from collections import defaultdict
from collections import deque
sys.setrecursionlimit(10**6)
INF = float("inf")


class Graph(object):
    """グラフを扱うオブジェクト
    """

    def __init__(self, N):
        self.N = N
        self.edges = defaultdict(list)
        pass

    def add_edges(self, from_, to_, weight):
        """必ず0インデックスで入力すること。
        """
        self.edges[from_].append([to_, weight])
        self.edges[to_].append([from_, weight])
        pass


def LCA_constract(g: Graph, root=0):
    """
    木gにおいて、頂点u, vのLCA(Lowest Common Ancestor)を求める
    g: 木。無向グラフとして与える。
    u, v:頂点
    root: 根
    元: https://tjkendev.github.io/procon-library/python/graph/lca-doubling.html
    """
    N = g.N
    LN = int(math.log2(g.N))

    ###
    # 各頂点の親 parと各頂点の深さdepthを求める
    ###
    par = [INF]*N
    depth = [INF]*N

    que = deque()
    que.append([root, 0, None])
    while len(que) > 0:
        curr, dep, pre = que.popleft()
        par[curr] = pre
        depth[curr] = dep
        for n, w in g.edges[curr]:
            if n != pre:
                que.append([n, dep+w, curr])

    ###
    # 祖先 ancの構築
    ###

    anc = [par]

    for i in range(LN):
        buf = [None]*N
        for j in range(N):
            if anc[i][j] == None:
                continue
            buf[j] = anc[i][anc[i][j]]
        anc.append(buf)
    return anc, depth


def LCA_query(anc, depth, u: int, v: int):
    ###
    # 共通祖先を求める
    ###
    N = len(depth)
    LN = int(math.log2(g.N))

    dd = depth[v] - depth[u]
    if dd < 0:
        u, v = v, u
        dd = -dd

    # assert depth[u] <= depth[v]
    for k in range(LN):
        if dd & 1:
            v = anc[k][v]
        dd >>= 1

    # assert depth[u] == depth[v]
    if u == v:
        return u

    for k in range(LN-1, -1, -1):
        pu = anc[k][u]
        pv = anc[k][v]
        if pu != pv:
            u = pu
            v = pv

    # assert anc[0][u] == anc[0][v]
    return anc[0][u]


def solve(N: int,
          a: "List[int]",
          b: "List[int]",
          c: "List[int]",
          Q: int,
          K: int,
          x: "List[int]",
          y: "List[int]"):

    g = Graph(N)
    for aa, bb, cc in zip(a, b, c):
        g.add_edges(*[aa-1, bb-1, cc])

    anc, depth = LCA_constract(g, root=K-1)

    for i in range(Q):
        print(depth[x[i]-1]+depth[y[i]-1])

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
    c = [int()] * (N-1)  # type: "List[int]"
    for i in range(N-1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    x = [int()] * (Q)  # type: "List[int]"
    y = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, a, b, c, Q, K, x, y)


if __name__ == '__main__':
    main()
