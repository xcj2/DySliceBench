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
n,m = LI()
print((n-1)*(m-1))
"""

#B
s = S()
print(s[0]+str(len(s)-2)+s[-1])
#C
"""
n = I()
a = LI()
d = [0,0]
for i in a:
    if i%2:
        d[0] += 1
    if i%4 == 0:
        d[1] += 1
if n % 2:
    d[0] -= 1
d[0] -= d[1]
if d[0] <= 0:
    print("Yes")
else:
    print("No")
"""

#D
"""
h,w = LI()
n = I()
a = LI()
c = [[None for x in range(w)] for y in range(h)]
i = 0
for y in range(h):
    if y%2:
        for x in range(w)[::-1]:
            if not a[i]:
                i += 1
            c[y][x] = i+1
            a[i] -= 1
    else:
        for x in range(w):
            if not a[i]:
                i += 1
            c[y][x] = i+1
            a[i] -= 1
for i in c:
    print(*i)
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
