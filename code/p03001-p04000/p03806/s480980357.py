#!usr/bin/env python3
from collections import defaultdict
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

#B

#C
"""
n,m = LI()
v = LIR(m)
p2 = [1]
for i in range(n):
    p2.append(p2[-1]*2)
dp = [[0 for i in range(p2[n])] for j in range(n)]
dp[0][1] = 1
for i in range(1,p2[n]):
    for k in range(n):
        for a,b in v:
            a -= 1
            b -= 1
            if k==a or k == b:
                c = p2[a]
                d = p2[b]
                if i&c and not i&d:
                    dp[b][i|d] += dp[k][i]
                if (not i&c) and i&d:
                    dp[a][i|c] += dp[k][i]
ans = 0
for i in range(1,n):
    ans += dp[i][-1]
print(ans)
"""

#D
n,p,q = LI()
v = [None for j in range(n)]
sa = 0
sb = 0
for i in range(n):
    a,b,c = LI()
    v[i] = [a,b,c]
    sa += a
    sb += b
dp = [[[float("inf") for i in range(sb+1)] for j in range(sa+1)] for k in range(n+1)]
dp[0][0][0] = 0
for i in range(n):
    for a in range(sa):
        for b in range(sb):
            ai,bi,ci = v[i]
            if a + ai <= sa and b + bi <= sb:
                dp[i+1][a+ai][b+bi] = min(dp[i+1][a+ai][b+bi],dp[i][a][b]+ci,dp[i][a+ai][b+bi])
            dp[i+1][a][b] = min(dp[i+1][a][b],dp[i][a][b])
li = [[p,q]]
while li[-1][0] <= sa and li[-1][1] <= sb:
    li.append([li[-1][0]+p,li[-1][1]+q])
li.pop(-1)
ans = float("inf")
for a,b in li:
    ans = min(ans,dp[n][a][b])
if ans == float("inf"):
    print(-1)
else:
    print(ans)
#E

#F

#G

#H

#I

#J

#K

#L

#M

#N

#O

#P

#Q

#R

#S

#T
