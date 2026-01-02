import sys, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from itertools import combinations, permutations, product
from heapq import heappush, heappop
from functools import lru_cache
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mat = lambda x, y, v: [[v]*y for _ in range(x)]
ten = lambda x, y, z, v: [mat(y, z, v) for _ in range(x)]
mod = 1000000007
sys.setrecursionlimit(1000000)

class UnionFind:
    # uf = UnionFind(N)
    # for x, y in pairs: uf.unite(x, y)
    # ans = max([uf.size(i) for i in range(N)])
    def __init__(self, n):
        self.n = n
        self.sizes = [1]*n
        self.parents = list(range(n))

    def find(self, x):
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return self.parents[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.sizes[x] < self.sizes[y]:
            x, y = y, x
        self.parents[y] = x
        self.sizes[x] += self.sizes[y]

N, Q = rl()
uf = UnionFind(N)
for i in range(Q):
    t, u, v = rl()
    u, v = u-1, v-1
    if t == 0:
        uf.unite(u, v)
    else:
        if uf.find(u) == uf.find(v):
            print(1)
        else:
            print(0)
