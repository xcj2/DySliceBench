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
a = LI()
ans = 0
k = a[0]
for i in range(1,n):
    if k*(k+a[i]) >= 0:
        if k < 0:
            ans += abs(1-k-a[i])
            a[i] = 1-k
            k = 1
        else:
            ans += abs(-1-k-a[i])
            a[i] = -1-k
            k = -1
    else:
        k += a[i]
print(ans)
"""

#D
x,y = LI()
if abs(x-y) <= 1:
    print("Brown")
else:
    print("Alice")
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
