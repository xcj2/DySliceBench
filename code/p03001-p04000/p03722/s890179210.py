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
def bellman_ford(start):
    dist = [float("inf") for i in range(n)]
    dist[start] = 0
    for i in range(n-1):
        update = False
        for j, k, l in adj:
                if dist[k] > dist[j] + l:
                    dist[k] = dist[j] + l
                    update = True
        if not update:
            break
    negative = [False for i in range(n)]
    for j, k, l in adj:
        if dist[k] > dist[j] + l:
            dist[k] = dist[j] + l
            negative[k] = True
    return dist,negative[n-1]
n,m = LI()
adj = []
for i in range(m):
    a,b,c = LI()
    a -= 1
    b -= 1
    adj.append([a,b,-c])
d,ne = bellman_ford(0)
if ne:
    print("inf")
else:
    print(-d[-1])
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
