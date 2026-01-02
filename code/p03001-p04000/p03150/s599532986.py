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
s = S()
n = len(s)
if s == list("keyence"):
    print("YES")
    quit()
for i in range(n):
    for j in range(i+1,n):
        if s[:i]+s[j:] == list("keyence"):
            print("YES")
            quit()
print("NO")
#B
"""
c = LIR(3)
v = [[] for i in range(4)]
for i in range(3):
    c[i][0] -= 1
    c[i][1] -= 1
    v[c[i][0]].append(c[i][1])
    v[c[i][1]].append(c[i][0])

for i in range(4):
    li = [True for i in range(4)]
    li[i] = False
    q = [i]
    c = 0
    while q:
        x = q.pop(-1)
        k = 0
        for j in v[x]:
            if li[j]:
                li[j] = False
                q.append(j)
                if k == 0:
                    c += 1
                    k += 1
    if c == 3:
        print("YES")
        quit()
print("NO")
"""

#C
"""
n = I()
ng = IR(3)
if n in ng:
    print("NO")
    quit()
ng.sort()
for i in range(100):
    b = n
    n -= 3
    if n in ng:
        while n in ng:
            n += 1
            if n == b:
                print("NO")
                quit()
if n <= 0:
    print("YES")
else:
    print("NO")
"""

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
