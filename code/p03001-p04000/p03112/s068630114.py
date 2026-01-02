#!usr/bin/env python3
import sys
from collections import defaultdict
from heapq import heappush, heappop
import math
import bisect
import random
def LI(): return list(map(int, input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return list(input())
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
mod = 1000000007

#A

#B

#C
"""
n,a,b,c = LI()
l = IR(n)
f = [True for i in range(3)]
ans = 0
for i in range(n):
    for d in range(3):
        if abs(l[i]-[a,b,c][d]) <= 10 and f[d]:
            ans += abs(l[i]-[a,b,c][d])
            f[d] = False
            l[i] = -float("inf")
k = False
for i in f:
    if i:
        k = True
        break
if not k:
    print(ans)
    quit()
"""
#D
a,b,q = LI()
s = IR(a)
t = IR(b)
for i in range(q):
    x = int(sys.stdin.readline())
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
