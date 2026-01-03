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
    n,k = LI()
    a = LI()
    d = defaultdict(lambda:0)
    for i in a:
        d[i] += 1
    d = list(d.values())
    d.sort()
    ans = 0
    for i in range(len(d)-k):
        ans += d[i]
    print(ans)
    return

#B
def B():
    n,z,w = LI()
    a = LI()
    if n == 1:
        print(abs(a[0]-w))
        return
    ans = max(abs(a[-1]-w),abs(a[-2]-a[-1]))
    print(ans)
    return

#C
def C():
    n = I()
    s1 = S()
    s2 = S()
    dp = [[[0]*3 for j in range(3)] for i in range(n+1)]
    if s1[0] == s2[0]:
        dp[1] = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
    else:
        dp[1] = [[0 if i == j else 1 for j in range(3)] for i in range(3)]
    for i in range(1,n):
        ni = i+1
        if s1[i] == s2[i]:
            for j in range(3):
                for k in range(3):
                    if k == j:continue
                    for l in range(3):
                        if l == j:continue
                        dp[ni][j][j] += dp[i][k][l]
        else:
            if i and s1[i] == s1[i-1]:
                for j in range(3):
                    for k in range(3):
                        dp[ni][j][k] = dp[i][j][k]
            else:
                for j in range(3):
                    for k in range(3):
                        if k == j:continue
                        for l in range(3):
                            if l == j:continue
                            for m in range(3):
                                if m == k:continue
                                dp[ni][j][k] += dp[i][l][m]
    ans = 0
    for i in range(3):
        for j in range(3):
            ans += dp[n][i][j]
    print(ans%mod)
    return

#D
def D():

    return

#E
def E():

    return

#Solve
if __name__ == "__main__":
    C()
