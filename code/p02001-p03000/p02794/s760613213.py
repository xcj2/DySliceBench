#!/usr/bin/env python3
import sys
INF = float("inf")

from collections import defaultdict
from collections import deque
import math


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.E = defaultdict(list)

    def add_edge(self, f, t, w=1):
        self.E[f].append((t, w))
        self.E[t].append((f, w))


class LCA(object):
    def __init__(self, g: Graph, root: int = 0):
        self.construct(g, root)

    def construct(self, g: Graph, root=0):
        """
        木gにおいて、頂点u, vのLCA(Lowest Common Ancestor)を求める
        g: 木。無向グラフとして与える。
        u, v:頂点
        root: 根
        元: https://tjkendev.github.io/procon-library/python/graph/lca-doubling.html
        """
        self.N = g.N
        self.LN = len(bin(g.N).lstrip("-0b"))

        # 各頂点の親 parと各頂点の深さdepthを求める
        par = [INF]*self.N
        self.depth = [INF]*self.N

        que = deque()
        que.append([root, 0, None])
        while len(que) > 0:
            curr, dep, pre = que.popleft()
            par[curr] = pre
            self.depth[curr] = dep
            for n, w in g.E[curr]:
                if n != pre:
                    que.append([n, dep+w, curr])

        # 祖先 ancの構築
        # anc[i][j]は頂点jの2**i個上の祖先を示す
        self.anc = [par]

        for i in range(self.LN):
            buf = [None]*self.N
            for j in range(self.N):
                if self.anc[i][j] == None:
                    continue
                buf[j] = self.anc[i][self.anc[i][j]]
            self.anc.append(buf)

        return

    def query(self, u: int, v: int):
        # 共通祖先を求める
        dd = self.depth[v] - self.depth[u]
        if dd < 0:
            u, v = v, u
            dd = -dd

        for k in range(self.LN):
            if dd & 1:
                v = self.anc[k][v]
            dd >>= 1

        if u == v:
            return u

        for k in range(self.LN-1, -1, -1):
            pu = self.anc[k][u]
            pv = self.anc[k][v]
            if pu != pv:
                u = pu
                v = pv

        return self.anc[0][u]


def bit_sum(n):
    return bin(n).count("1")


def solve(N: int, a: "List[int]", b: "List[int]",
          M: int, u: "List[int]", v: "List[int]"):

    g = Graph(N)
    for X, Y in zip(a, b):
        g.add_edge(X-1, Y-1)
    # LCAを使う
    lca = LCA(g)

    # 条件を与える頂点を結ぶパスをbit列で与える
    paths = []
    for j in range(M):
        path = 0
        a1 = u[j]-1
        a2 = v[j]-1
        p = lca.query(a1, a2)
        while a1 != p:
            path |= 1 << (a1-1)
            a1 = lca.anc[0][a1]
        while a2 != p:
            path |= 1 << (a2-1)
            a2 = lca.anc[0][a2]
        paths.append(path)
    # print([bin(p) for p in paths])

    ans = 2**(N-1)
    for p in range(1, 1 << M):
        spider_net = 0
        strp = bin(p).lstrip("0b")
        # print("パターン", strp)
        for i, c in enumerate(strp[::-1]):
            if c == "1":
                spider_net |= paths[i]
        C = bit_sum(spider_net)
        # print(C, bin(spider_net))
        if bit_sum(p) % 2 == 1:
            ans -= 2**(N-1-C)
        else:
            ans += 2**(N-1-C)
    print(ans)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    M = int(next(tokens))  # type: int
    u = [int()] * (M)  # type: "List[int]"
    v = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, a, b, M, u, v)


if __name__ == '__main__':
    main()
