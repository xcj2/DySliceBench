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
a,b,c,d = LI()
print(max(a*b,c*d))
#B

#C
"""
def factor(n):
    i = 2
    m = n
    while m >= i:
        while m%i == 0:
            m //= i
            d[i] += 1
            d[i] %= mod
            if m < i:break
        i += 1
n = I()
d = defaultdict(int)
for i in range(2,n+1):
    factor(i)
ans = 1
for i in d.values():
    ans *= i+1
    ans %= mod
print(ans)
"""

#D
"""
n,a,b = LI()
x = LI()
ans = 0
for i in range(n-1):
    if a*(x[i+1]-x[i]) > b:
        ans += b
    else:
        ans += a*(x[i+1]-x[i])
print(ans)
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
