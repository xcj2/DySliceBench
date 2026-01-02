import os
import sys

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


class UnionFind:
    def __init__(self, size=None, nodes=None):
        """
        size か nodes どっちか指定。
        nodes は set、size は list を使う。
        set の最悪計算量は O(N) なので size 指定のほうが若干速い
        :param int size:
        :param collections.Iterable nodes:
        """
        assert size is not None or nodes is not None
        if size is not None:
            self._parents = [i for i in range(size)]
            self._ranks = [0 for _ in range(size)]
            self._sizes = [1 for _ in range(size)]
        else:
            self._parents = {k: k for k in nodes}
            self._ranks = {k: 0 for k in nodes}
            self._sizes = {k: 1 for k in nodes}

    def unite(self, x, y):
        """
        x が属する木と y が属する木を併合
        :param x:
        :param y:
        :return:
        """
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return

        # rank が小さい方が下
        if self._ranks[x] > self._ranks[y]:
            # x が root
            self._parents[y] = x
            self._sizes[x] += self._sizes[y]
        else:
            # y が root
            self._parents[x] = y
            self._sizes[y] += self._sizes[x]
            if self._ranks[x] == self._ranks[y]:
                self._ranks[y] += 1

    def root(self, x):
        """
        x が属する木の root
        :param x:
        :return:
        """
        if self._parents[x] == x:
            return x
        self._parents[x] = self.root(self._parents[x])
        return self._parents[x]

    def size(self, x):
        """
        x が属する木のノード数
        :param x:
        :return:
        """
        return self._sizes[self.root(x)]


N, M = list(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))
XY = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

uf = UnionFind(size=N)
for x, y in XY:
    uf.unite(x, y)

# N-M 個の木がある
if N - M == 1:
    print(0)
    exit()
if (N - M - 1) * 2 > N:
    print('Impossible')
    exit()

A = np.array(A, dtype=int)
idx = A.argsort()

ans = 0
cnt = 0
used_n = np.zeros(N, dtype=bool)
used_root = np.zeros(N, dtype=bool)
for i in idx:
    if not used_root[uf.root(i)]:
        used_root[uf.root(i)] = True
        used_n[i] = True
        ans += A[i]
        cnt += 1

for i in idx:
    if not used_n[i]:
        ans += A[i]
        cnt += 1
    if cnt >= (N - M - 1) * 2:
        break
print(ans)
