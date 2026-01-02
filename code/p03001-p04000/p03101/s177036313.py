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
h,w = LI()
y,x = LI()
print(h*w-h*x-w*y+y*x)
#B
"""
n,m,c = LI()
b = LI()
a = LIR(n)
ans = 0
for i in range(n):
    d = c
    for k in range(m):
        d += b[k]*a[i][k]
    if d > 0:
        ans += 1
print(ans)
"""


#C

"""
n,m = LI()
v = LIR(n)
v.sort(key = lambda x:x[0])
ans = 0
k = 0
for a,b in v:
    if k+b >= m:
        ans += (m-k)*a
        print(ans)
        quit()
    ans += b*a
    k += b
"""
#D
#a,b = LI()

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
