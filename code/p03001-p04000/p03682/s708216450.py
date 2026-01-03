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

#D
def root(x):
    if x == par[x]:
        return x
    par[x] = root(par[x])
    return par[x]

def same(x,y):
    return root(x) == root(y)

def unite(x,y):
    x = root(x)
    y = root(y)
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
n = I()
v = LIR(n)
l = []
for i in range(n):
    v[i].append(i)
par = [i for i in range(n)]
rank = [0 for i in range(n)]
v.sort(key = lambda x:x[0])
for i in range(n-1):
    l.append([v[i][2],v[i+1][2],v[i+1][0]-v[i][0]])
v.sort(key = lambda x:x[1])
for i in range(n-1):
    l.append([v[i][2],v[i+1][2],v[i+1][1]-v[i][1]])
l.sort(key = lambda x:x[2])
k = 0
ans = 0
for i in range(len(l)):
    x,y,c = l[i]
    if not same(x,y):
        k += 1
        ans += c
        unite(x,y)
    if k == n-1:break
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
