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
    def root(x):
        if par[x] == x:
            return par[x]
        r = root(par[x])
        d[x] += d[par[x]]
        par[x] = r
        return par[x]
    def same(x,y):
        return root(x) == root(y)
    def weight(x):
        root(x)
        return d[x]
    def unite(x,y,w):
        w += weight(x)
        w -= weight(y)
        x = root(x)
        y = root(y)
        if rank[x] < rank[y]:
            par[x] = y
            d[x] = -w
        else:
            par[y] = x
            d[y] = w
            if rank[x] == rank[y]:
                rank[x] += 1

    n,m = LI()
    par = [i for i in range(n)]
    rank = [0 for i in range(n)]
    d = [0 for i in range(n)]
    for i in range(m):
        x,y,w = LI()
        x -= 1
        y -= 1
        if same(x,y):
            if weight(y)-weight(x) != w:
                print("No")
                quit()
        else:
            unite(x,y,w)
    print("Yes")
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
