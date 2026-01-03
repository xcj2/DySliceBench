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
x = I()
ans = 2*(x//11)+1
x %= 11
if x == 0:
    ans -= 1
if x > 6:
    ans += 1
print(ans)
"""

#D
n = I()
a = LI()
d = defaultdict(int)
for i in a:
    d[i] += 1
l = list(d.keys())
i = 0
while i < len(l):
    if d[l[i]] < 2:
        l.pop(i)
        i -= 1
    i += 1
l.sort()
k = 0
for i in l:
    k ^= ~(d[i]%2)
    d[i] = 1
ans = sum(list(d.values()))
ans -= 1 if k%2 else 0
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
