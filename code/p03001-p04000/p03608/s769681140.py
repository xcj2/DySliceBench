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
inf = float('INF')

#A
def A():
    n, m, R = LI()
    r = LI_()
    edg = [[inf] * n for i in range(n)]
    for _ in range(m):
        a, b, c = LI_()
        c += 1
        edg[a][b] = c
        edg[b][a] = c
    for i in range(n):
        edg[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                edg[i][j] = min(edg[i][j], edg[i][k] + edg[k][j])
    fulls = itertools.permutations(range(R), R)
    ans = inf
    for full in fulls:
        b = -1
        tmp = 0
        for f in full:
            if b == -1:
                b = r[f]
                continue
            tmp += edg[r[f]][b]
            b = r[f]
        ans = min(ans, tmp)
    print(ans)

    return

#B
def B():
    return

#C
def C():
    return

#D
def D():
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    A()
