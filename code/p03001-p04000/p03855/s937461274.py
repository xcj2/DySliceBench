import os
import sys
from collections import defaultdict

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18

N, K, L = list(map(int, sys.stdin.readline().split()))
P, Q = list(zip(*[map(int, sys.stdin.readline().split()) for _ in range(K)]))
R, S = list(zip(*[map(int, sys.stdin.readline().split()) for _ in range(L)]))


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
        x = self.find(x)
        y = self.find(y)
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

    def find(self, x):
        """
        x が属する木の root
        :param x:
        :return:
        """
        if self._parents[x] == x:
            return x
        self._parents[x] = self.find(self._parents[x])
        return self._parents[x]

    def size(self, x):
        """
        x が属する木のノード数
        :param x:
        :return:
        """
        return self._sizes[self.find(x)]


uf1 = UnionFind(size=N + 1)
for p, q in zip(P, Q):
    uf1.unite(p, q)
uf2 = UnionFind(size=N + 1)
for r, s in zip(R, S):
    uf2.unite(r, s)

counts = defaultdict(int)
for i in range(1, N + 1):
    counts[(uf1.find(i), uf2.find(i))] += 1

ans = []
for i in range(1, N + 1):
    ans.append(counts[(uf1.find(i), uf2.find(i))])
print(' '.join(map(str, ans)))
