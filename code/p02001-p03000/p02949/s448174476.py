#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
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
def IR(n):
    res = [None] * n
    for i in range(n):
        res[i] = II()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI()
    return res
def FR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR_(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI_()
    return res
def SR(n):
    res = [None] * n
    for i in range(n):
        res[i] = S()
    return res
def LSR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LS()
    return res
mod = 1000000007
inf = float('INF')

#solve
def solve():
    n, m, p = LI()
    edg = [[] for i in range(n)]
    for _ in range(m):
        a, b, c = LI_()
        c += 1
        edg[a].append((b, c))
    dp = [-inf] * n
    dp[0] = 0
    for j in range(n):
        for i in range(n):
            score = dp[i]
            for e, s in edg[i]:
                if dp[e] < score + s - p:
                    dp[e] = score + s - p
    ans = dp[:]
    for j in range(n):
        for i in range(n):
            score = dp[i]
            for e, s in edg[i]:
                if dp[e] < score + s - p:
                    dp[e] = inf
    if ans[-1] != dp[-1]:
        print(-1)
    else:
        print(abs(max(ans[-1],0)))
    return


#main
if __name__ == '__main__':
    solve()
