#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heapify,heappush, heappop
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
    for i in range(n):l[i] = LS()
    return l
sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    return

#B
def B():
    return

#C
def C():
    return

#D
def D():
    n,k = LI()
    g = LIR(n)
    g.sort(key = lambda x:-x[1])
    f = [0 for i in range(n+1)]
    x = 0
    ans = 0
    c = []
    for i in range(k):
        ans += g[i][1]
        if not f[g[i][0]]:x+=1
        else:c.append(g[i][1])
        f[g[i][0]] += 1
    ans += x**2
    c.sort()
    c = deque(c)
    d = ans
    for i in range(k,n):
        if not c:
            break
        if f[g[i][0]]:continue
        d += g[i][1]-c.popleft()+2*x+1
        f[g[i][0]] = 1
        x += 1
        if d > ans:
            ans = d
    print(ans)
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
    D()
