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
s = S()
for i in range(len(s)):
    if not i%2:
        print(s[i],end = "")
print()
#C
"""
n = I()
d = defaultdict(int)
a = LI()
for i in a:
    d[i] += 1
    d[i+1] += 1
    d[i-1] += 1
d = list(d.values())
print(max(d))
"""

#D
"""
n = I()
a = LI()
k = 0
for i in range(n-1):
    if a[i] == i+1:
        x = a[i]
        a[i] = a[i+1]
        a[i+1] = x
        k += 1
if a[n-1] == n:k += 1
print(k)
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
