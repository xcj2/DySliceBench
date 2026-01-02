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
    N, a, b = LI()
    ans = pow(2, N, mod) - 1
    dp = [0] * (max(a, b) + 1)
    dp[0] = 1
    for i in range(max(a, b)):
        dp[i + 1] = (dp[i] * (N - i)) * pow(i + 1, mod - 2, mod)
        dp[i + 1] %= mod
    print((ans-dp[a]-dp[b]) % mod)
    return


#main
if __name__ == '__main__':
    solve()
