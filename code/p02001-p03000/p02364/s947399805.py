import sys
import math
import string
import fractions
import random
from operator import itemgetter
import itertools
from collections import deque
import copy
import heapq
import bisect

MOD = 10 ** 9 + 7
INF = float('inf')
input = lambda: sys.stdin.readline().strip()


def minimum_spanning_tree(n, info):
    """
    頂点の数:nと辺の情報i:infoから最小全域木([[辺の始点の頂点,辺の終点の頂点, 重み], ...])を返す。
    info:[[辺の始点の頂点,辺の終点の頂点, 重み], ...](bellman_ford()の入力形式)
    """
    ans = []
    info.sort(key=itemgetter(2))

    class UnionFind:
        def __init__(self, n):
            self.n = n
            self.parents = [-1] * n

        def find(self, x):
            if self.parents[x] < 0:
                return x
            else:
                self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)

            if x == y:
                return

            if self.parents[x] > self.parents[y]:
                x, y = y, x

            self.parents[x] += self.parents[y]
            self.parents[y] = x

        def size(self, x):
            return -self.parents[self.find(x)]

        def same(self, x, y):
            return self.find(x) == self.find(y)

        def members(self, x):
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root]

        def roots(self):
            return [i for i, x in enumerate(self.parents) if x < 0]

        def group_count(self):
            return len(self.roots())

        def all_group_members(self):
            return {r: self.members(r) for r in self.roots()}

        def __str__(self):
            return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    uf = UnionFind(n)
    for i in info:
        if not uf.same(i[0], i[1]):
            ans.append(i)
            uf.union(i[0], i[1])
    return ans


V, E = map(int, input().split())
stw = [list(map(int, input().split())) for _ in range(E)]
print(sum([i[2] for i in minimum_spanning_tree(V, stw)]))

