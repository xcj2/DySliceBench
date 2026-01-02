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
    h,w = LI()
    a = [sys.stdin.readline() for i in range(h)]
    s = 0
    p = [None for i in range(w*h)]
    q = [None for j in range(w*h)]
    l = 0
    for i in range(h):
        for j in range(w):
            if a[i][j] == "#":
                p[s] = (i,j)
                s += 1
            else:
                q[l] = (i,j)
                l += 1
    if s == h*w:
        print(0)
        quit()
    ans = 0
    M = w*h
    for i,j in q[:h*w-s]:
        m = M
        for x,y in p[:s]:
            if abs(i-x)+abs(j-y) < m:
                m = abs(i-x)+abs(j-y)
        if m > ans:
            ans = m
    print(ans)
    return

#B
def B():
    h,w,n = LI()
    sy,sx = LI()
    sy -= 1
    sx -= 1
    s = S()
    t = S()
    ks = list("LRUD")
    kt = list("RLDU")
    ds = [[0,-1],[0,1],[-1,0],[1,0]]
    dt = [[0,1],[0,-1],[1,0],[-1,0]]
    for i in range(4):
        y,x = [sy,sx]
        for j in range(n):
            if s[j] == ks[i]:
                y+=ds[i][0]
                x+=ds[i][1]
                if y < 0 or y >= h or x < 0 or x >= w:
                    print("NO")
                    quit()
            if t[j] == kt[i]:
                y += dt[i][0]
                x += dt[i][1]
                if y < 0:y = 0
                elif y >= h:y = h-1
                elif x < 0:x=0
                elif x >= w:x=w-1
    print("YES")
    return

#C
def C():
    n = I()
    return

#D
def D():
    n = I()
    return

#E
def E():
    n = I()
    return

#F
def F():
    n = I()
    return

#Solve
if __name__ == "__main__":
    B()
