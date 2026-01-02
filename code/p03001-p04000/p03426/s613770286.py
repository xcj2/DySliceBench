#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    n = II()
    print(n//3)
    return

#B
def B():
    _ = II()
    s = S()
    print(["Three", "Four"][len(set(s)) - 4])
    return

#C
def C():
    return

class Value_UnionFind():
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.differ_weight = [0] * n
        self.rank = [0] * n

    def root(self,x):
        if x == self.par[x]:
            return x
        r = self.root(self.par[x])
        self.differ_weight[x] += self.differ_weight[self.par[x]]
        self.par[x] = r
        return r

    def weight(self, x):
        self.root(x)
        return self.differ_weight[x]

    def unit(self, x, y, w):
        w += self.weight(x)
        w -= self.weight(y)
        x = self.root(x)
        y = self.root(y)
        if x == y: return False
        if self.rank[x] < self.rank[y]: x, y, w = y, x, -w
        if self.rank[x] == self.rank[y]: self.rank[x] += 1
        self.par[y] = x
        self.differ_weight[y] = w
        return True

    def differ(self, x, y):
        return self.weight(y) - self.weight(x)
#D
def D():
    h, w, d = LI()
    u = Value_UnionFind(h * w)
    field = defaultdict(list)
    for i in range(h):
        a = LI_()
        for j in range(w):
            field[a[j]] = [j, i]
    for i in range(h * w):
        if i + d < h * w:
            x1, y1 = field[i]
            x2, y2 = field[i + d]
            u.unit(i, i + d, abs(x1 - x2) + abs(y1 - y2))

    for _ in range(II()):
        l, r = LI_()
        print(u.differ(l, r))
    return

#Solve
if __name__ == '__main__':
    D()
