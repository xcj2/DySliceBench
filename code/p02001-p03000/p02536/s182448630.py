# coding=utf-8
from math import floor, ceil, sqrt, factorial, log, gcd, log10
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement, chain
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heappushpop, heapify
from copy import copy, deepcopy
import sys
INF = float('inf')
mod = 10**9+7
sys.setrecursionlimit(10 ** 6)


def lcm(a, b): return a * b / gcd(a, b)


def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
# 1 2 3
# a, b, c = LI()


def I(): return int(sys.stdin.buffer.readline())
# a = I()


def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
# abc def
# a, b = LS()


def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
# a = S()


def IR(n): return [I() for i in range(n)]
# 2
# 1
# 2
# [1, 2]


def LIR(n): return [LI() for i in range(n)]
# 2
# 1 2 3
# 4 5 6
# [[1,2,3], [4,5,6]]


def SR(n): return [S() for i in range(n)]
# 2
# abc
# def
# [abc, def]


def LSR(n): return [LS() for i in range(n)]
# 2
# abc def
# ghi jkl
# [[abc,def], [ghi,jkl]]


def SRL(n): return [list(S()) for i in range(n)]
# 2
# abcd
# efgh
# [[a,b,c,d], [e,f,g,h]]


class UnionFind():
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


n, m = LI()
uf = UnionFind(n)
for _ in range(m):
    a, b = LI()
    uf.union(a-1, b-1)
print(uf.group_count()-1)
