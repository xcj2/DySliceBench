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
n = I()
print((n*(n+1))//2)
"""
#B
s = S()
ans = []
for i in s:
    if i == "0":
        ans.append(0)
    if i == "1":
        ans.append(1)
    if i == "B" and ans:
        ans.pop(-1)
for i in ans:
    print(i,end = "")
print()
#C

#D
"""
s = S()
l = len(s)
for i in range(l-1):
    if s[i] == s[i+1]:
        print(i+1,i+2)
        quit()
for i in range(l-2):
    if s[i] == s[i+2]:
        print(i+1,i+3)
        quit()
print(-1,-1)
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
