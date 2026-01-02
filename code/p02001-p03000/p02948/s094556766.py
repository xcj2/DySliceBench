import sys
sys.setrecursionlimit(10000000)
def input():
    return sys.stdin.readline()[:-1]
from bisect import *
from collections import *
from heapq import *
from fractions import Fraction

class UnionFind:

    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.height = [0 for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def getsize(self, x):
        return self.size[self.find(x)]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.height[x] < self.height[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = self.par[x]
            self.size[x] += self.size[y]
            if self.height[x] == self.height[x]:
                self.height[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

class BIT:
    def __init__(self, N):
        self.N = N
        self.bit = [0 for _ in range(N+1)]
    def add(self, x, a):
        while x <= self.N:
            self.bit[x] += a
            x += x & -x
    def sum(self, x):
        ret = 0
        while x > 0:
            ret += self.bit[x]
            x -= x & -x
        return ret

N, M = map(int, input().split())
ab = sorted([list(map(int, input().split())) for i in range(N)], key=lambda x: -x[1])
ans, bit, uf = 0, BIT(M), UnionFind(M+2)
for a, b in ab:
    i = M-a+1
    if 0 < i and bit.sum(i) < i:
        ans += b
        if bit.sum(i-1) == bit.sum(i):
            lb, ub = i, i+1
        else:
            lb, ub = 0, i
            while lb+1 < ub:
                mid = (lb+ub)//2
                if uf.same(mid, ub):
                    ub = mid
                else:
                    lb = mid
        bit.add(lb, 1)
        uf.unite(lb, ub)
print(ans)
