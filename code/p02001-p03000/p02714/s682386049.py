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
    n = II()
    s = S()
    dpr = [0] * (n + 1)
    dpg = [0] * (n + 1)
    dpb = [0] * (n + 1)
    for i in range(n):
        dpr[i + 1] = dpr[i]
        dpg[i + 1] = dpg[i]
        dpb[i + 1] = dpb[i]
        if s[i] == "R":
            dpr[i+1] += 1
        elif s[i] == "G":
            dpg[i+1] += 1
        else:
            dpb[i + 1] += 1
    ans = 0

    for i in range(1, n - 1):
        if s[i] == "R":
            ans += dpg[i] * (dpb[-1] - dpb[i+1])
            ans += dpb[i] * (dpg[-1] - dpg[i+1])
        elif s[i] == "G":
            ans += dpb[i] * (dpr[-1] - dpr[i+1])
            ans += dpr[i] * (dpb[-1] - dpb[i+1])
        else:
            ans += dpg[i] * (dpr[-1] - dpr[i + 1])
            ans += dpr[i] * (dpg[-1] - dpg[i + 1])
    for j in range(1, n - 1):
        for i in range(1, j + 1):
            if j + i >= n:
                continue
            if s[j-i] != s[j] and s[j] != s[j + i] and s[j-i] != s[j + i]:
                ans -= 1
    print(ans)
                
    return


#main
if __name__ == '__main__':
    solve()
