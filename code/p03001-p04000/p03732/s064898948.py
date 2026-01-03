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
""""
n,T = LI()
ans = 0
t = LI()
for i in range(n-1):
    ans += min(T,t[i+1]-t[i])
ans += T
print(ans)
"""

#D
n,w = LI()
g = LIR(n)
l = [[] for i in range(4)]
for W,v in g:
    l[W-g[0][0]].append(v)
    l[W-g[0][0]].sort(reverse = True)
l0 = len(l[0])
l1 = len(l[1])
l2 = len(l[2])
l3 = len(l[3])
for i in range(l0-1):
    l[0][i+1] += l[0][i]
l[0].insert(0,0)
for i in range(l1-1):
    l[1][i+1] += l[1][i]
l[1].insert(0,0)
for i in range(l2-1):
    l[2][i+1] += l[2][i]
l[2].insert(0,0)
for i in range(l3-1):
    l[3][i+1] += l[3][i]
l[3].insert(0,0)
ans = 0
for i in range(l0+1):
    for j in range(l1+1):
        for k in range(l2+1):
            for m in range(l3+1):
                if i*g[0][0]+j*(g[0][0]+1)+k*(g[0][0]+2)+m*(g[0][0]+3) <= w:
                    ans = max(ans,l[0][i]+l[1][j]+l[2][k]+l[3][m])
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
