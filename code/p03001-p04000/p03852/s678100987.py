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
c = input()
if c in "aiueo":
    print("vowel")
else:
    print("consonant")
#B

#C
"""
s = input()
while s:
    if s[:11] == "dreameraser":
        s = s[11:]
    elif s[:10] == "dreamerase":
        s = s[10:]
    elif s[:7] == "dreamer":
        s = s[7:]
    elif s[:6] == "eraser":
        s = s[6:]
    elif s[:5] == "dream":
        s = s[5:]
    elif s[:5] == "erase":
        s = s[5:]
    else:
        print("NO")
        quit()
print("YES")
"""

#D
"""
def root(x,par,rank):
    if x == par[x]:
        return x
    par[x] = root(par[x],par,rank)
    return par[x]
def unite(x,y,par,rank):
    x = root(x,par,rank)
    y = root(y,par,rank)
    if x == y:return
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
n,k,l = LI()
par1 = [i for i in range(n)]
rank1 = [0 for i in range(n)]
par2 = [i for i in range(n)]
rank2 = [0 for i in range(n)]
for i in range(k):
    p,q = LI()
    p -= 1
    q -= 1
    unite(p,q,par1,rank1)
for i in range(l):
    p,q = LI()
    p -= 1
    q -= 1
    unite(p,q,par2,rank2)
d = {}
for i in range(n):
    k = (root(i,par1,rank1),root(i,par2,rank2))
    if k in d:
        d[k] += 1
    else:
        d[k] = 1
ans = []
for i in range(n):
    k = (root(i,par1,rank1),root(i,par2,rank2))
    ans.append(d[k])
print(*ans)
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
