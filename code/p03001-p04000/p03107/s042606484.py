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
a,b,c = LI()
print(min(b//a,c))
"""

#B
"""
a,b,k = LI()
i = 1
ans = [1]
while i <= min(a,b):
    i += 1
    if a%i == 0 and b%i == 0:
        ans.append(i)
print(ans[-k])
"""

#C
s = list(map(int,S()))
print(2*min(sum(s),len(s)-sum(s)))

#D
"""
def root(x):
    if par[x] == x:
        return x
    par[x] = root(par[x])
    return par[x]
def unite(x,y):
    x = root(x)
    y = root(y)
    if x == y:
        ans.append(ans[-1])
        return
    sx = s[x]
    sy = s[y]
    if rank[x] < rank[y]:
        par[x] = y
        s[y] += sx
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
        s[x] += sy
    ans.append(ans[-1]+sx*sy)
n,m  = LI()
v = LIR(m)
v = v[::-1]
par = [i for i in range(n)]
rank = [0 for i in range(n)]
s = [1 for i in range(n)]
ans = [0]
k = n*(n-1)//2
v.pop(-1)
for a,b in v:
    if ans[0] == k:
        ans.append(k)
        continue
    a -= 1
    b -= 1
    unite(a,b)
for i in ans[::-1]:
    print(k-i)
"""
#E
"""
n,a,b = LI()
s = input()
ans = 0
i = 0
while i < n:
    j = i+1
    if s[i:j] in s[:i]:
        while s[i:j] in s[:i]:
            j += 1
            if j >= n-1:break
        ans += min(b,a*(j-i))
    else:
        ans += a*(j-i)
    i = j
print(ans)
"""
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
