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
inf = float("INF")

#solve
def solve():
    n, m, s = LI()
    uvab = LIR(m)
    cd = LIR(n)
    dp = [[inf] * 2501 for i in range(n)]
    edg = [[] for i in range(n)]
    for u, v, a, b in uvab:
        edg[u - 1].append((v - 1, a, b))
        edg[v - 1].append((u - 1, a, b))
    for i, (c, d) in enumerate(cd):
        edg[i].append((i, -c, d))
    if s >= 2501:
        s = 2500
    q = [(0, 0, s)]
    dp[0][s] = 0
    time = 0
    while q:
        time, p, score = heappop(q)
        for e, a, b in edg[p]:
            timebuf = time
            if 0 <= score - a <= 2500:
                timebuf += b
                if dp[e][score - a] > timebuf:
                    dp[e][score - a] = timebuf
                    heappush(q, (timebuf, e, score - a))
                    for i in range(score - a, -1, -1):
                        if dp[e][i] > timebuf:
                            dp[e][i] = timebuf
                        else:
                            break
    
    for i in range(1, n):
        print(min(dp[i]))

    return


#main
if __name__ == '__main__':
    solve()
