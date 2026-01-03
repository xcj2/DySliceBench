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
n,k,x,y = IR(4)
print(min(k,n)*x+max(n-k,0)*y)
#B

#C
"""
n,a = LI()
x = LI()
s = sum(x)
dp = [[[0 for i in range(s+1)] for j in range(n+1)] for k in range(n+1)]
for i in range(n+1):
    dp[i][0][0] = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(s+1):
            if k >= x[i-1]:
                dp[i][j][k] = dp[i-1][j][k]+dp[i-1][j-1][k-x[i-1]]
            else:
                dp[i][j][k] = dp[i-1][j][k]
ans = 0
for i in range(1,n+1):
    if a*i <= s:
        ans += dp[n][i][a*i]
print(ans)
"""

#D
"""
def f(b,n):
    m = n
    res = 0
    while m > 0:
        res += m%b
        m //= b
    return res
n,s = IR(2)
if n == s:
    print(n+1)
    quit()
if n == 1:
    print(-1)
    quit()
k = int(n**0.5)
for b in range(2,k+1):
    if f(b,n) == s:
        print(b)
        quit()
for p in range(1,k+1)[::-1]:
    if (n-s)%p == 0:
        b = (n-s)//p+1
        if b != 0:
            if f(b,n) == s:
                print(b)
                quit()
print(-1)
"""
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
