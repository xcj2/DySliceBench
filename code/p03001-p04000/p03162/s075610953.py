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
    n = I()
    h = LI()
    dp = [float("inf") for i in range(n)]
    dp[0] = 0
    for i in range(n-2):
        dp[i+1] = min(dp[i+1],dp[i]+abs(h[i+1]-h[i]))
        dp[i+2] = min(dp[i+2],dp[i]+abs(h[i+2]-h[i]))
    dp[n-1] = min(dp[n-1],dp[n-2]+abs(h[n-1]-h[n-2]))
    print(dp[n-1])
#B
def B():
    n,k = LI()
    h = LI()
    dp = [float("inf") for i in range(n)]
    dp[0] = 0
    for i in range(n):
        for j in range(1,min(n-i,k+1)):
            dp[i+j] = min(dp[i+j],dp[i]+abs(h[i+j]-h[i]))
    print(dp[n-1])

#C
def C():
    n = I()
    v = LIR(n)
    dp = [[0,0,0] for i in range(n+1)]
    for i in range(n):
        dp[i+1][0] = max(dp[i+1][0],dp[i][1]+v[i][0],dp[i][2]+v[i][0])
        dp[i+1][1] = max(dp[i+1][1],dp[i][2]+v[i][1],dp[i][0]+v[i][1])
        dp[i+1][2] = max(dp[i+1][2],dp[i][0]+v[i][2],dp[i][1]+v[i][2])
    print(max(dp[n]))

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
