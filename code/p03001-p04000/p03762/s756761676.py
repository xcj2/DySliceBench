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
n = I()
s = SR(n)
for i in range(n):
    for j in range(len(s[i])):
        while s[i][j] in s[i][:j]:
            s[i][j] = "0"+s[i][j]
ans = set(s[0])
for i in range(1,n):
    ans &= set(s[i])
ans = sorted(list(ans))
if len(ans) == 0:print()
else:
    for i in range(len(ans)):
        ans[i] = ans[i][-1]
    ans.sort()
    for i in range(len(ans)-1):
        print(ans[i],end = "")
    print(ans[-1])
"""

#D
n,m = LI()
ln = [n-1]
lm = [m-1]
a = n-1
b = m-1
while a > 2:
    a -= 2
    ln.append(ln[-1]+a)
while b > 2:
    b -= 2
    lm.append(lm[-1]+b)
la = len(ln)
lb = len(lm)
for i in range(la):
    if i or a == 2:
        ln.append(ln[la-i-1])
for i in range(lb):
    if i or b == 2:
        lm.append(lm[lb-i-1])
x,y = LIR(2)
lx = 0
ly = 0
for i in range(n-1):
    lx += ln[i]*(x[i+1]-x[i])%mod
    lx %= mod
for i in range(m-1):
    ly += lm[i]*(y[i+1]-y[i])%mod
    ly %= mod
ans = lx*ly%mod
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
