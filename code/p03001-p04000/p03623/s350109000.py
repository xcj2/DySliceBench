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
x,a,b = LI()
if abs(a-x) < abs(b-x):
    print("A")
else:
    print("B")
#B

#C
"""
n = I()
d = defaultdict(int)
a = LI()
for i in a:
    d[i] += 1
d = list(d.items())
d.sort(key = lambda x:-x[0])
l = 0
k = 0
for i,j in d:
    if j >= 2:
        if l == 0:
            l = i
        else:
            k = i
        if j >= 4:
            k = i
    if k != 0:break
print(l*k)
"""

#D
"""
n = I()
s1 = S()
s2 = S()
ans = 0
i = 0
key = 1
d = defaultdict(int)
while i < n:
    if s1[i] == s2[i]:
        if not d[s1[i]]:
            d[s1[i]] = 1
            if i == 0:
                ans = 3
            else:
                if key:
                    ans *= 2
        key = 1
    else:
        if not d[s1[i]] and not d[s2[i]]:
            d[s1[i]] = 1
            d[s2[i]] = 1
            if i == 0:
                ans = 6
            else:
                if key:
                    ans *= 2
                else:
                    ans *= 3
        if not d[s1[i]]:
            d[s1[i]] = 1
            if not key:
                ans *= 2
        if not d[s2[i]]:
            d[s2[i]] = 1
            if not key:
                ans *= 2
        key = 0
        i += 1
    i += 1
    ans %= mod
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
