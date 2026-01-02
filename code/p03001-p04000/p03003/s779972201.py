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
    for i in range(n):l[i] = LS()
    return l
sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    x,n = LI()
    if x < n:
        print(0)
    else:
        print(10)
    return

#B
def B():
    n,x = LI()
    l = LI()
    d = 0
    ans = 1
    for i in range(n):
        d += l[i]
        if d <= x:
            ans += 1
    print(ans)
    return

#C
def C():
    w,h,x,y = LI()
    ans = w*h/2
    k = 0
    if x == w/2 and y == h/2:
        k = 1
    print(ans,k)
    return

#D
def D():
    n,k = LI()
    a = LI()
    b = [a[i] for i in range(n)]
    for i in range(n-1):
        b[i+1] += b[i]
    b.insert(0,0)
    ans = 0
    for l in range(n):
        r = bisect.bisect_left(b,b[l]+k)
        ans += n-r+1
    print(ans)
    return

#E
def E():
    n,m = LI()
    s = LI()
    t = LI()
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for j in range(m+1):
        dp[0][j] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+mod
            if dp[i][j] >= mod:
                dp[i][j] %= mod
    print(dp[n][m])
    return

#F
def F():
    return

#Solve
if __name__ == "__main__":
    E()
