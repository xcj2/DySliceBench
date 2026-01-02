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
    h,w,D = LI()
    a = LIR(h)
    d = defaultdict(int)
    for y in range(h):
        for x in range(w):
            d[a[y][x]] = y*w+x
    n = h*w
    dist = [[0 for i in range(n//D+1)] for i in range(D)]
    for i in range(1,n-D+1):
        y = d[i]//w
        x = d[i]%w
        y_ = d[i+D]//w
        x_ = d[i+D]%w
        k = i%D
        j = i//D
        dist[k][j+1] = dist[k][j]+abs(y_-y)+abs(x_-x)
    q = I()
    for i in range(q):
        l,r = LI()
        k = l%D
        print(dist[k][r//D]-dist[k][l//D])
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
