#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS():return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = I()
    return l
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LI()
    return l
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = S()
    return l
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = SR()
    return l
mod = 1000000007

#A
def A():
    return

#B
def B():
    return

#C
def C():
    n,x,y,z = LI()
    po2 = [1<<i for i in range(x+y+z+1)]
    max = po2[x+y+z]
    ng = po2[x+y+z-1]|po2[y+z-1]|po2[z-1]
    dp = [[0 for i in range(max)] for i in range(n+1)]
    dp[0][0] = 1
    mask = max-1
    for i in range(n):
        for j in range(max):
            for k in range(1,11):
                t = j<<k|1<<(k-1)
                if t&ng != ng:
                    t &= mask
                    dp[i+1][t] += dp[i][j]
                    dp[i+1][t] %= mod
    ans = pow(10,n,mod)
    for i in range(max):
        ans -= dp[n][i]
        ans %= mod
    print(ans)


#D
def D():
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

#Solve
if __name__ == "__main__":
    C()
