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
    a = LI()
    if n == 3:
        print(max(a))
        return
    dp = [[-inf] * 3 for i in range(n + 1)]
    dp[0] = [0, 0, 0]
    dp[1][0] = a[0]
    dp[2][1] = a[1]
    for i in range(3, n+1):
        dp[i][0] = dp[i - 2][0] + a[i-1]
        dp[i][1] = max(dp[i - 2][1], dp[i - 3][0]) + a[i-1]
        dp[i][2] = max(dp[i - 2][2], dp[i - 3][1], dp[i - 4][0]) + a[i-1]
    if n & 1:
        print(max(dp[-3][0], dp[-2][1], dp[-1][2]))
    else:
        print(max(dp[-1][1], dp[-2][0]))
    return


#main
if __name__ == '__main__':
    solve()
