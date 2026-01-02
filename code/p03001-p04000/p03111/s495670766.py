#!usr/bin/env python3
from collections import defaultdict
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return list(sys.stdin.readline())
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
mod = 1000000007

#A

#B

#C
def dfs(n,k):
    if n == 0:
        li.append(k)
    else:
        for i in range(4):
            dfs(n-1,k+[i])
n,a,b,c = LI()
l = IR(n)
li = []
dfs(n,[])
ans = float("inf")
for k in li:
    d = [0,0,0]
    m = 0
    for i in range(n):
        if k[i] < 3:
            if d[k[i]] != 0:
                m += 10
            d[k[i]] += l[i]
    if d[0]*d[1]*d[2] == 0:continue
    m += abs(a-d[0])+abs(b-d[1])+abs(c-d[2])
    ans = min(ans, m)
print(ans)
#D
"""
a,b,q = LI()
s = IR(a)
t = IR(b)
for i in range(q):
    x = I()
    c = bisect.bisect_left(s,x)
    ans = float("inf")
    if c == a:
        k = abs(x-s[-1])
        y = s[-1]
        d = bisect.bisect_left(t,y)
        if d == b:
            k += abs(y-t[-1])
        else:
            if abs(y-t[d-1]) < abs(y-t[d]):
                k += abs(y-t[d-1])
            else:
                k += abs(y-t[d])
        ans = min(k,ans)
    else:
        k = abs(x-s[c-1])
        y = s[c-1]
        d = bisect.bisect_left(t,y)
        if d == b:
            k += abs(y-t[-1])
        else:
            if abs(y-t[d-1]) < abs(y-t[d]):
                k += abs(y-t[d-1])
            else:
                k += abs(y-t[d])
        ans = min(k,ans)
        k = abs(x-s[c])
        y = s[c]
        d = bisect.bisect_left(t,y)
        if d == b:
            k += abs(y-t[-1])
        else:
            if abs(y-t[d-1]) < abs(y-t[d]):
                k += abs(y-t[d-1])
            else:
                k += abs(y-t[d])
        ans = min(k,ans)
    c = bisect.bisect_left(t,x)
    if c == b:
        k = abs(x-t[-1])
        y = t[-1]
        d = bisect.bisect_left(s,y)
        if d == a:
            k += abs(y-s[-1])
        else:
            if abs(y-s[d-1]) < abs(y-s[d]):
                k += abs(y-s[d-1])
            else:
                k += abs(y-s[d])
        ans = min(k,ans)
    else:
        k = abs(x-t[c-1])
        y = t[c-1]
        d = bisect.bisect_left(s,y)
        if d == a:
            k += abs(y-s[-1])
        else:
            if abs(y-s[d-1]) < abs(y-s[d]):
                k += abs(y-s[d-1])
            else:
                k += abs(y-s[d])
        ans = min(k,ans)
        k = abs(x-t[c])
        y = t[c]
        d = bisect.bisect_left(s,y)
        if d == a:
            k += abs(y-s[-1])
        else:
            if abs(y-s[d-1]) < abs(y-s[d]):
                k += abs(y-s[d-1])
            else:
                k += abs(y-s[d])
        ans = min(k,ans)
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
