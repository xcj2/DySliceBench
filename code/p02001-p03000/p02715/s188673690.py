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
    n, k = LI()
    dp = [0] * (k + 1)
    for i in range(k, 0, -1):
        if i < 3:
            dp[i] += pow(k // i, n, mod)
            dp[i] %= mod
            if i != 1:
                dp[1] -= dp[i]
                dp[1] %= mod
        else:
            dp[i] += pow(k // i, n, mod)
            dp[i] %= mod
            j = 2
            while j ** 2 <= i:
                if i % j == 0:
                    dp[j] -= dp[i]
                    dp[j] %= mod
                    m = i // j
                    if m != j:
                        dp[m] -= dp[i]
                        dp[m] %= mod
                j += 1
            dp[1] -= dp[i]
            dp[1] %= mod
    ans = 0
    for i in range(k + 1):
        ans += i * dp[i]
        ans %= mod
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
