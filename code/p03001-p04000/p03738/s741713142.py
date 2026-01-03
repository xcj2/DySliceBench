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
"""
s = LS()
print(s[0][0].upper()+s[1][0].upper()+s[2][0].upper())
"""
#B
a,b = IR(2)
if a < b:
    print("LESS")
elif a == b:
    print("EQUAL")
else:
    print("GREATER")
#C
"""
n = I()
a = LI()
b = [a[i] for i in range(n)]
ans = 0
k = a[0]
if a[0] == 0:
    a[0] = 1
    ans = 1
    k = 1
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
if b[0] >= 0:
    ans2 = b[0]+1
    k = -1
    b[0] = -1
else:
    ans2 = 1-b[0]
    k = 1
    b[0] = 1
for i in range(1,n):
    if k*(k+b[i]) >= 0:
        if k < 0:
            ans2 += abs(1-k-b[i])
            b[i] = 1-k
            k = 1
        else:
            ans2 += abs(-1-k-b[i])
            b[i] = -1-k
            k = -1
    else:
        k += b[i]
print(min(ans,ans2))
"""
#D
"""
x,y = LI()
if abs(x-y) <= 1:
    print("Brown")
else:
    print("Alice")
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
