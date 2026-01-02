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
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
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
    n, m, k = LI()
    ab = LIR_(m)
    cd = LIR_(k)
    par = [i for i in range(n)]
    size = [1] * n
    def root(x):
        if x == par[x]:
            return x
        par[x] = root(par[x])
        return par[x]

    def unite(a, b):
        a = root(a)
        b = root(b)
        if size[a] > size[b]: a, b = b, a
        if a == b: return False
        par[a] = b
        size[b] += size[a]
        return True

    lis = [1] * n
    for a, b in ab:
        unite(a, b)
        lis[a] += 1
        lis[b] += 1
    for c, d in cd:
        if root(c) == root(d):
            lis[c] += 1
            lis[d] += 1
    for i in range(n):
        print(size[root(i)] - lis[i], end=" ")
    print()
    return


#main
if __name__ == '__main__':
    solve()
