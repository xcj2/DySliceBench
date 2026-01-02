#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
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
    n = list(map(int, input()))
    K = I()
    l = len(n)
    if l < K:
        print(0)
        return
    dp = [[[0 for k in range(l+1)] for j in range(2)] for i in range(l+1)]
    dp[0][0][0] = 1
    for i in range(l):
        ni = i+1
        for j in range(2):
            for k in range(l):
                x = 9 if j else n[i]
                for d in range(x+1):
                    nk = k+(d!=0)
                    nj = j or d < n[i]
                    if nk <= l:
                        dp[ni][nj][nk] += dp[i][j][k]
    
    print(dp[l][0][K]+dp[l][1][K])
    return

#Solve
if __name__ == "__main__":
    solve()
