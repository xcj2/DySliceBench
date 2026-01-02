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

#C
"""
n = I()
d = defaultdict(int)
for i in range(n):
    a = I()
    d[a] ^= 1
d = list(d.values())
print(sum(d))
"""
#D
def dfs(n,k,l,a):
    if n == 0:
        a.append(l)
    for i in range(n):
        dfs(n-1,k[:i]+k[i+1:],l+[k[i]],a)
n,m,R = LI()
r = LI()
f = [i for i in range(n)]
for i in range(R):
    r[i] -= 1
v = [[float("inf") for j in range(n)] for i in range(n)]
for i in range(n):
    v[i][i] = 0
for i in range(m):
    a,b,c = LI()
    a -= 1
    b -= 1
    v[a][b] = c
    v[b][a] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            v[i][j] = min(v[i][j],v[i][k]+v[k][j])
l = []
dfs(R,r,[],l)
ans = float("inf")
for k in l:
    d = 0
    for i in range(R-1):
        d += v[k[i]][k[i+1]]
    ans = min(ans,d)
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
