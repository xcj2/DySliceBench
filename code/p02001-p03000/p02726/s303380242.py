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
    n, x, y = LI()
    dist = [[inf] * n for i in range(n)]
    edg = [[] for i in range(n)]
    for i in range(1, n):
        edg[i].append(i - 1)
        edg[i - 1].append(i)
    edg[x - 1].append(y - 1)
    edg[y - 1].append(x - 1)
    for i in range(n):
        dist[i][i] = 0
        q = [(0, i)]
        while q:
            s, p = heappop(q)
            for e in edg[p]:
                if dist[i][e] > dist[i][p] + 1:
                    dist[i][e] = dist[i][p] + 1
                    heappush(q, (dist[i][e], e))
    ans = [0] * n
    for i in range(n):
        for j in range(n):
            if dist[i][j] != inf:
                ans[dist[i][j]] += 1
    for ai in ans[1:]:
        print(ai//2)
    
    return


#main
if __name__ == '__main__':
    solve()
