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
        self.cnt = 0
        self.pre = [None]*self.size
        self.low = [None]*self.size
        self.par = [None]*self.size
        self.bridge = []
        for x in range(self.size):
            if self.pre[x] is None:
                self.pre[x] = self.low[x] = self.cnt
                self.dfs(x)

    def dfs(self, x):
        for y in self.v[x]:
            if self.pre[y] is None:
                self.cnt += 1
                self.pre[y] = self.low[y] = self.cnt
                self.par[y] = x
                py = self.dfs(y)
                if py < self.low[x]:
                    self.low[x] = py
            else:
                if self.par[x] != y and self.pre[y] < self.low[x]:
                    self.low[x] = self.pre[y]
            if self.pre[x] < self.low[y]:
                self.bridge.append((x,y))

        return self.low[x]

    def bridge(self):
        return self.bridge

def solve():
    n,m = LI()
    v = [[] for i in range(n)]
    for i in range(m):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
    ans = LowLink(v)
    print(len(ans.bridge))
    return

#Solve
if __name__ == "__main__":
    solve()
