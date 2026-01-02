#!usr/bin/env python3
from collections import defaultdict, deque, Counter, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from heapq import heappush, heappop, heapify

import itertools
import math, fractions
import sys, copy

def L(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline().rstrip())
def SL(): return list(sys.stdin.readline().rstrip())
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI1(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return [list(x) for x in sys.stdin.readline().split()]
def R(n): return [sys.stdin.readline().strip() for _ in range(n)]
def LR(n): return [L() for _ in range(n)]
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def LIR1(n): return [LI1() for _ in range(n)]
def SR(n): return [SL() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

def perm(n, r): return math.factorial(n) // math.factorial(r)
def comb(n, r): return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

def make_list(n, *args, default=0): return [make_list(*args, default=default) for _ in range(n)] if len(args) > 0 else [default for _ in range(n)]

dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MOD = 1000000007
INF = float("inf")

sys.setrecursionlimit(1000000)

class UnionFind:
    def __init__(self, n):
        self._parent = [i for i in range(n)]
        self._rank = [0 for _ in range(n)]
        self._group_size = [1 for _ in range(n)]
        self.num_of_groups = n

    def find(self, x):
        # vs = []
        while self._parent[x] != x:
            # vs.append(x)
            x = self._parent[x]
        # for v in vs: self._parent[v] = x
        return x

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return
        if self._rank[px] < self._rank[py]:
            self._parent[px] = py
            self._group_size[py] += self._group_size[px]
        else:
            self._parent[py] = px
            self._group_size[px] += self._group_size[py]
        if self._rank[px] == self._rank[py]:
            self._rank[py] += 1
        self.num_of_groups -= 1

    def is_same(self, x, y): return self.find(x) == self.find(y)
    def group_size(self, x): return self._group_size[self.find(x)]


def main():
    N, Q = LI()
    TUV = LIR(Q)

    uf = UnionFind(N+1)

    for t, u, v in TUV:
        if t == 0:
            uf.union(u, v)
        else:
            print(int(uf.is_same(u, v)))

if __name__ == '__main__':
    main()