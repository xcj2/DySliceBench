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

#B

#C
"""
n = I()
a = LI()
b = [None for i in range(n-1)]
for i in range(n-1):
    a[i+1] += a[i]
for i in range(n-1):
    b[i] = abs(2*a[i]-a[n-1])
print(min(b))
"""

#D
n = I()
v = [[] for i in range(n)]
for i in range(n-1):
    a,b = LI()
    a -= 1
    b -= 1
    v[a].append(b)
    v[b].append(a)
d_f = [-1 for i in range(n)]
q = []
q.append(0)
d_f[0] = 0
while q:
    x = q.pop(-1)
    for y in v[x]:
        if d_f[y] == -1:
            d_f[y] = d_f[x] + 1
            q.append(y)
d_s = [-1 for i in range(n)]
q.append(n-1)
d_s[n-1] = 0
while q:
    x = q.pop(-1)
    for y in v[x]:
        if d_s[y] == -1:
            d_s[y] = d_s[x] + 1
            q.append(y)
f = 0
s = 0
for i in range(n):
    if d_f[i] <= d_s[i]:
        f += 1
    else:
        s += 1
if f > s:
    print("Fennec")
else:
    print("Snuke")
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
