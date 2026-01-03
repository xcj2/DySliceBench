#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    n = I()
    a = LI()
    u = [0]*n
    r = 1
    for l in range(n):
        if l == r:
            r += 1
        while r < n and a[r-1] <= a[r]:
            r += 1
        u[l] = r
    d = [0]*n
    r = 1
    for l in range(n):
        if l == r:
            r += 1
        while r < n and a[r-1] >= a[r]:
            r += 1
        d[l] = r
    i = 0
    for t in range(n):
        i = max(u[i],d[i])
        if i == n:
            print(t+1)
            return
    return
#B
def B():
    n,m = LI()
    v = [[] for i in range(n)]
    for i in range(m):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
    f = [1]*n
    p = deque([0])
    f[0] = 0
    update = 1
    while update:
        update = 0
        x = p[0]
        for y in v[x]:
            if f[y]:
                update = 1
                f[y] = 0
                p.appendleft(y)
                break
        x = p[-1]
        for y in v[x]:
            if f[y]:
                update = 1
                f[y] = 0
                p.append(y)
                break
    p = list(p)
    for i in range(len(p)):
        p[i] += 1
    print(len(p))
    print(*p)
    return

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

#Solve
if __name__ == "__main__":
    B()
