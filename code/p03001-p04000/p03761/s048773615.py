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
n = I()
s = SR(n)
for i in range(n):
    for j in range(len(s[i])):
        while s[i][j] in s[i][:j]:
            s[i][j] = "0"+s[i][j]
ans = set(s[0])
for i in range(1,n):
    ans &= set(s[i])
ans = sorted(list(ans))
if len(ans) == 0:print()
else:
    for i in range(len(ans)):
        ans[i] = ans[i][-1]
    ans.sort()
    for i in range(len(ans)-1):
        print(ans[i],end = "")
    print(ans[-1])
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
