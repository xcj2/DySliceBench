#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
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

#A
def A():
    def f(n):
        a = str(n)
        l = len(a)
        dp = [[[0]*2 for i in range(2)] for j in range(l+1)]
        dp[0][0][0] = 1
        for i in range(l):
            ni = i+1
            for j in range(2):
                x = 9 if j else int(a[i])
                for k in range(2):
                    for d in range(x+1):
                        nj = j|(d < int(a[i]))
                        nk = k|(d in (4,9))
                        dp[ni][nj][nk] += dp[i][j][k]
        return dp[l][0][1]+dp[l][1][1]

    a,b = LI()
    print(f(b)-f(a-1))
    return

#B
def B():
    D = I()
    n = list(map(int, input()))
    l = len(n)
    dp = [[[0]*2 for i in range(D)] for j in range(l+1)]
    dp[0][0][0] = 1
    for i in range(l):
        ni = i+1
        for j in range(D):
            for k in range(2):
                x = 9 if k else int(n[i])
                for d in range(x+1):
                    nj = (j+d)%D
                    nk = k|(d < int(n[i]))
                    dp[ni][nj][nk] += dp[i][j][k]
                    dp[ni][nj][nk] %= mod
    print((dp[l][0][0]+dp[l][0][1]-1)%mod)
    return

#C
def C():
    n = list(map(int, input()))
    l = len(n)
    dp = [[[0]*2 for j in range(l+1)] for i in range(l+1)]
    dp[0][0][0] = 1
    for i in range(l):
        ni = i+1
        for j in range(l):
            for k in range(2):
                x = 9 if k else n[i]
                for d in range(x+1):
                    nj = j+(d == 1)
                    nk = k|(d < n[i])
                    dp[ni][nj][nk] += dp[i][j][k]
    ans = 0
    for i in range(l+1):
        ans += i*sum(dp[l][i])
    print(ans)
    return

#D
def D():
    n = list(map(int, input()))
    l = len(n)
    D = I()
    dp = [[[0]*2 for i in range(D)] for i in range(l+1)]
    dp[0][0][0] = 1
    for i in range(l):
        for j in range(D):
            for k in range(2):
                x = 9 if k else n[i]
                for d in range(x+1):
                    ni = i+1
                    nj = (j+d)%D
                    nk = k|(d<n[i])
                    dp[ni][nj][nk] += dp[i][j][k]
                    dp[ni][nj][nk] %= mod
    print((sum(dp[l][0])-1)%mod)
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

#I
def I_():

    return

#J
def J():

    return

#K
def K():

    return

#Solve
if __name__ == "__main__":
    D()
