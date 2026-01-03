#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

#solve
def solve():
    n, m = LI()
    par = [i for i in range(n)]
    def root(x):
        if x == par[x]:
            return x
        par[x] = root(par[x])
        return par[x]
    def unite(x, y):
        x = root(x)
        y = root(y)
        if y < x: x, y = y, x
        par[y] = x
        return
    ling = [[] for i in range(m)]
    for i in range(n):
        kl = LI()
        for l in kl[1:]:
            ling[l-1].append(i)
    for l in ling:
        if l:
            l0 = l[0]
            for li in l[1:]:
                unite(l0, li)
    for i in range(n):
        root(i)
    print("YES" if len(set(par)) == 1 else "NO")
    return


#main
if __name__ == '__main__':
    solve()
