#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    h,w,k = LI()
    dp = [[0]*w for _ in range(h+1)]
    dp[0][0] = 1
    k -= 1
    f = [1,1]
    for i in range(w):
        f.append(f[-1]+f[-2])

    for i in range(h):
        ni = i+1
        for j in range(w):
            dpj = dp[i][j]
            nj = j+1
            if nj < w:
                l = f[j]
                r = f[w-1-nj]
                dp[ni][nj] += l*r*dpj%mod
            l = f[j]
            r = f[w-1-j]
            dp[ni][j] += l*r*dpj%mod
            nj = j-1
            if nj >= 0:
                l = f[nj]
                r = f[w-1-j]
                dp[ni][nj] += l*r*dpj%mod
    print(dp[h][k]%mod)
    return

#Solve
if __name__ == "__main__":
    solve()
