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
    n, k = LI()
    rsp = LI()
    t = S()
    dp = [[0] * 3 for i in range(n + k)]
    j = ["r", "s", "p"]
    for i in range(n):
        ti = t[i]
        for l in range(3):
            dp[i + k][l] = max(dp[i][(l - 1) % 3], dp[i][(l + 1) % 3]) + (rsp[l] if (j.index(ti) - 1) % 3 == l else 0)

    ans = 0
    for i in range(k):
        ans += max(dp[n + i])
    print(ans)

    return


#main
if __name__ == '__main__':
    solve()
