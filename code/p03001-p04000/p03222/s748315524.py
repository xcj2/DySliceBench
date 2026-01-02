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
    n,m = LI()
    v = LIR(m)
    for i in range(m):
        v[i] = [v[i][0],v[i][1],i]
    v.sort(key = lambda x:x[1])
    f = [0 for i in range(n+1)]
    ans = [None for i in range(m)]
    for p,y,i in v:
        f[p] += 1
        s = "{:0>6}".format(p)
        t = "{:0>6}".format(f[p])
        ans[i] = s+t
    for i in ans:
        print(i)
#D
def D():
    h,w,k = LI()
    dp = [[0 for i in range(w)] for j in range(h+1)]
    dp[0][0] = 1
    p = [1 for i in range(w+1)]
    for i in range(w):
        p[i+1] = p[i]*2
    l = [i for i in range(p[w-1])]
    i = 0
    while i < len(l):
        a = l[i]
        for j in range(w):
            if a&p[j] and a&p[j+1]:
                l.pop(i)
                i -= 1
                break
        i += 1
    d = [[0 for i in range(3)] for j in range(w)]
    for j in range(w):
        for s in l:
            if 0 < j < w-1:
                if p[j]&s:
                    d[j][2] += 1
                elif p[j-1]&s:
                    d[j][0] += 1
                else:
                    d[j][1] += 1
            elif j == 0:
                if p[j]&s:
                    d[j][2] += 1
                else:
                    d[j][1] += 1
            else:
                if p[j-1]&s:
                    d[j][0] += 1
                else:
                    d[j][1] += 1
    for i in range(h):
        for j in range(w):
            dp[i+1][j] += d[j][1]*dp[i][j]
            dp[i+1][j] %= mod
            if j > 0:
                dp[i+1][j-1] += d[j][0]*dp[i][j]
                dp[i+1][j-1] %= mod
            if j < w-1:
                dp[i+1][j+1] += d[j][2]*dp[i][j]
                dp[i+1][j+1] %= mod
    print(dp[h][k-1])
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
    D()
