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
"""
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)
n = I()
a = IR(n)
l = a[0]
for i in range(1,n):
    g = gcd(l,a[i])
    l *= a[i]//g
print(l)
"""

#B
n = I()
v = [[] for i in range(n)]
for i in range(n-1):
    a,b,c = LI()
    a -= 1
    b -= 1
    v[a].append([b,c])
    v[b].append([a,c])
Q,k = LI()
d = [-1 for i in range(n)]
d[k-1] = 0
q = deque()
q.append(k-1)
while q:
    x = q.pop()
    for y,c in v[x]:
        if d[y] == -1:
            d[y] = d[x]+c
            q.append(y)
for i in range(Q):
    x,y = LI()
    x -= 1
    y -= 1
    print(d[x]+d[y])
#C

#D

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
