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
a,b = LI()
if a+b >= 10:
    print("error")
else:
    print(a+b)
#B

#C
"""
n = I()
s = IR(n)
su = sum(s)
dp = [[0 for i in range(su+1)] for j in range(n)]
dp[0][s[0]] = 1
for i in range(n):
    dp[i][0] = 1
for i in range(1,n):
    for j in range(su+1)[::-1]:
        if s[i]+j <= su:
            dp[i][s[i]+j] = max(dp[i][s[i]+j],dp[i-1][j])
        dp[i][j] = max(dp[i][j],dp[i-1][j])
for i in range(su+1)[::-1]:
    if dp[n-1][i] == 1 and i%10 != 0:
        break
print(i)
"""

#D
"""
n,a,b = LI()
h = IR(n)
l = 0
r = math.ceil(max(h)/b)
while r-l > 1:
    m = (l+r)//2
    k = 0
    for i in range(n):
        k += max(0,math.ceil((h[i]-b*m)/(a-b)))
        if k > m:break
    if k > m:
        l = m
    else:
        r = m
print(r)
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
