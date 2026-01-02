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
    n,k = LI()
    a = LI()
    m = max(k,max(a)).bit_length()
    f = [0]*m
    for i in a:
        for j in range(m):
            if i&(1<<j):
                f[j] += 1
    dp = [[-float("inf")]*2 for i in range(m+1)]
    dp[0][0] = 0
    for i in range(m):
        ni = i+1
        ki = (k>>(m-i-1))&1
        for j in range(2):
            x = 1 if j else ki
            for d in range(x+1):
                nj = j|(d<ki)
                dp[ni][nj] = max(dp[ni][nj], dp[i][j]+(d*(n-f[m-i-1])+(1-d)*f[m-i-1])*(1<<(m-i-1)))
    print(max(dp[m]))
    return

#F
def F():
    def bit_count(n):
        return bin(n).count("1")
    a,K = LI()
    a = list(map(int, str(a)))
    l = len(a)
    m = 1024
    dp = [[[float("inf")]*2 for j in range(m)] for i in range(l+1)]
    dp[0][0][0] = 0
    for i in range(l):
        ni = i+1
        for j in range(m):
            if bit_count(j) > K:continue
            for k in range(2):
                x = 9 if k else a[i]
                for d in range(x+1):
                    nj = j|(1<<d)
                    nk = k|(d<a[i])
                    c = dp[i][j][k]*10+a[i]-d
                    if c < dp[ni][nj][nk]:
                        dp[ni][nj][nk] = c
    ans = float("inf")
    for i in range(m):
        if bit_count(i) <= K:
            mi = min(dp[l][i])
            if mi < ans:
                ans = mi
    dp = [[[float("inf")]*2 for j in range(m)] for i in range(l+1)]
    dp[0][0][0] = 0
    for i in range(l):
        ni = i+1
        for j in range(m):
            if bit_count(j) > K:continue
            for k in range(2):
                x = 0 if k else a[i]
                for d in range(x,10):
                    nj = j|(1<<d)
                    nk = k|(d>a[i])
                    c = dp[i][j][k]*10+d-a[i]
                    if c < dp[ni][nj][nk]:
                        dp[ni][nj][nk] = c
    for i in range(m):
        if bit_count(i) <= K:
            mi = min(dp[l][i])
            if mi < ans:
                ans = mi
    print(ans)
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
