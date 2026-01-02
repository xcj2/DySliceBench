#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

class LowLink:
    def __init__(self, v):
        self.size = len(v)
        self.v = v
        self.pre = [None]*self.size
        self.low = [None]*self.size
        self.articulation = []
        self.bridge = []
        for x in range(self.size):
            if self.pre[x] is None:
                self.cnt = 0
                self.dfs(x,None)

    def dfs(self, x, par):
        self.pre[x] = self.low[x] = self.cnt
        self.cnt += 1
        is_articulation = False
        n = 0
        for y in self.v[x]:
            if self.pre[y] is None:
                n += 1
                lowy = self.dfs(y, x)
                if lowy < self.low[x]:
                    self.low[x] = lowy
                if self.pre[x] <= lowy:
                    if self.pre[x]:
                        is_articulation = True
                    if self.pre[x] < lowy:
                        self.bridge.append((x,y))
            else:
                if par != y and self.pre[y] < self.low[x]:
                    self.low[x] = self.pre[y]

        if par is None and n > 1:
            is_articulation = True

        if is_articulation:
            self.articulation.append(x)

        return self.low[x]


def solve():
    n,m = LI()
    v = [[] for i in range(n)]
    for i in range(m):
        a,b = LI()
        v[a].append(b)
        v[b].append(a)
    lowlink = LowLink(v)
    for i in sorted(lowlink.articulation):
        print(i)
    return

#Solve
if __name__ == "__main__":
    solve()

