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
    x,y,z = LI()
    for i in range(1000000)[::-1]:
        if i*y+(i+1)*z <= x:
            print(i)
            quit()
    return

#E
def E():
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    h,w = LI()
    s = SR(h)
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                su = 0
                for dy,dx in d:
                    y = i+dy
                    x = j+dx
                    if 0 <= y < h and 0 <= x < w:
                        if s[y][x] == "#":
                            su += 1
                if su == 0:
                    print("No")
                    quit()
    print("Yes")
    return

#F
def F():
    a,b,c,X,Y = LI()
    ans = float("inf")
    for z in range(300001):
        if z%2 == 0:
            m = c*z
            x = z//2
            y = z//2
            m += a*max(0,X-x)
            m += b*max(0,Y-y)
            if m < ans:
                ans = m
    print(ans)
    return

#G
def G():
    n = I()
    x = LI()
    f = [(i,x[i]) for i in range(n)]
    f.sort(key = lambda x:x[1])
    g = [(f[i][0],i) for i in range(n)]
    g.sort(key = lambda x:x[0])
    for i in range(n):
        if g[i][1] < n//2:
            print(f[n//2][1])
        else:
            print(f[n//2-1][1])
    return

#H
def H():
    return

#I
def I_():
    return

#J
def J():
    return

#Solve
if __name__ == "__main__":
    D()
