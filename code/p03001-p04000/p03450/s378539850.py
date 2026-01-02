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
    a, b, c = IR(3)
    a -= b
    print(a % c)
    return

#B
def B():
    a, b, c, x, ans = II(), II(), II(), II(), 0
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                if i * 500 + j * 100 + k * 50 == x:
                    ans += 1
    print(ans)
    return

#C
def C():
    n = II()
    a = LI()
    dp = [[0] * (n + 1) for i in range(2)]
    for i in range(1, n + 1):
        dp[0][i] += dp[0][i - 1] + a[i - 1]
    a = LI()
    for i in range(1, n + 1):
        dp[1][i] = max(dp[0][i], dp[1][i - 1]) + a[i - 1]
    print(dp[1][-1])
    
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
    n, m = LI()
    u = Value_UnionFind(n)
    for _ in range(m):
        l, r, d = LI_()
        if not u.unit(l, r, d + 1):
            if u.differ(l, r) != d + 1:
                print("No")
                return
    print("Yes")


    return

#Solve
if __name__ == '__main__':
    D()
