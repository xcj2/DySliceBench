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
n = input()
print("ABC"+n)
#B

#C
"""
def dijkstra():
    d[0] = 0
    q = [[0,0]]
    while q:
        dx, x = heappop(q)
        for y in v[x]:
            if d[y] > dx+1:
                d[y] = dx+1
                heappush(q,[d[y],y])
n,m = LI()
v = [[] for i in range(n)]
for i in range(m):
    a,b = LI()
    a -= 1
    b -= 1
    v[a].append(b)
    v[b].append(a)
d = [float("inf") for i in range(n)]
dijkstra()
if d[n-1] <= 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
"""

#D
"""
k = I()
ans = [i+k//50 for i in range(50)]
k %= 50
for i in range(k):
    ans[i] += 51
    for j in range(50):
        ans[j] -= 1
print(50)
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
