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
def A():
    n = I()
    s = S()
    d = defaultdict(int)
    for i in s:
        d[i] += 1
    ans = 1
    for i in d.keys():
        ans *= d[i]+1
        ans %= mod
    print(ans-1)
#B
def B():
    n = I()
    c = IR(n)
    v = [[i+1] for i in range(n-1)]
    v.append([])
    d = defaultdict(deque)
    for i in range(n):
        d[c[i]].append(i)
    for i in d.keys():
        x = None
        while d[i]:
            y = d[i].popleft()
            if x != None and y != x+1:
                v[x].append(y)
            x = y
    path = [0]*(n)
    path[0] = 1
    q = [0]
    while q:
        x = heappop(q)
        for y in v[x]:
            if path[y] == 0:
                heappush(q,y)
            path[y] += path[x]
            path[y] %= mod
    print(path[-1])
#C
def C():
    return

#D
def D():
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == "__main__":
    B()
