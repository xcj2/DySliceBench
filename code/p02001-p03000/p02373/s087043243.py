# -*- coding: utf-8 -*-
from functools import lru_cache
import sys
buff_readline = sys.stdin.buffer.readline
readline = sys.stdin.readline

INF = 2**60


def read_int():
    return int(buff_readline())


def read_int_n():
    return list(map(int, buff_readline().split()))


class Doubling():
    def __init__(self, a0):
        """
        a0 is an array-like object which contains ai, 0 <= i < N.
        ai is the next value of i.
        """
        N = len(a0)
        self.N = N
        self.nt = [[None] * N for i in range(N.bit_length()+1)]
        for i, a in enumerate(a0):
            self.nt[0][i] = a

        for i in range(1, len(self.nt)):
            for j in range(N):
                if self.nt[i-1][j] is None:
                    self.nt[i][j] = None
                else:
                    self.nt[i][j] = self.nt[i-1][self.nt[i-1][j]]

    def apply(self, i, n):
        """
        Apply n times from i
        """
        j = i
        for k in range(n.bit_length()):
            m = 1 << k
            if m & n:
                j = self.nt[k][j]
            if j is None:
                break
        return j


class LCA():
    def __init__(self, g, root):
        s = [root]
        self.N = len(g)
        self.p = [None] * self.N
        self.d = [INF] * self.N

        self.p[root] = root
        self.d[root] = 0
        while s:
            u = s.pop()
            for v in g[u]:
                if self.d[v] is INF:
                    self.p[v] = u
                    self.d[v] = self.d[u] + 1
                    s.append(v)

        self.doubling = Doubling(self.p)

    def query(self, u, v):
        if self.d[u] > self.d[v]:
            u, v = v, u
        o = self.d[v] - self.d[u]
        v = self.doubling.apply(v, o)

        if u == v:
            return u

        for k in range(len(self.doubling.nt)-1, -1, -1):
            if self.doubling.nt[k][u] != self.doubling.nt[k][v]:
                u = self.doubling.nt[k][u]
                v = self.doubling.nt[k][v]
        return self.doubling.nt[0][u]


def slv(N, KC, Q, UV):
    g = [list() for _ in range(N)]
    for u, (k, *c) in enumerate(KC):
        for v in c:
            g[u].append(v)
            g[v].append(u)

    lca = LCA(g, 0)

    ans = []
    for u, v in UV:
        i = lca.query(u, v)
        ans.append(i)

    return ans


def main():
    N = read_int()
    KC = [read_int_n() for _ in range(N)]
    Q = read_int()
    UV = [read_int_n() for _ in range(Q)]
    print(*slv(N, KC, Q, UV), sep='\n')


if __name__ == '__main__':
    main()

