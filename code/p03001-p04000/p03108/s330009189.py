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


def comb(n, k):
    if n % 2 == 0:
        return n / 2 * (n - 1)
    else:
        return (n - 1) / 2 * n


N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
uf = UnionFind(N)
ans = deque()
ans.appendleft(int(comb(N, 2)))
for i in range(M - 1, 0, -1):
    size1 = uf.size(AB[i][0] - 1)
    size2 = uf.size(AB[i][1] - 1)
    if size1 == N:
        ans.appendleft(0)
    elif uf.same(AB[i][0] - 1, AB[i][1] - 1):
        ans.appendleft(ans[0])
    else:
        uf.union(AB[i][0] - 1, AB[i][1] - 1)
        size3 = uf.size(AB[i][0] - 1)
        if size1 + size2 == 2:
            ans.appendleft(ans[0] - 1)
        elif size1 == 1:
            ans.appendleft(ans[0] - (int(comb(size3, 2)) - int(comb(size2, 2))))
        elif size2 == 1:
            ans.appendleft(ans[0] - (int(comb(size3, 2)) - int(comb(size1, 2))))
        else:
            ans.appendleft(ans[0] - (int(comb(size3, 2)) - int(comb(size1, 2)) - int(comb(size2, 2))))
for i in ans:
    print(i)
