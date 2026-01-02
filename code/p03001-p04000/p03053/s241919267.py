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
    p = deque()
    M = w*h
    d = [[-1 for i in range(w)] for j in range(h)]
    for i in range(h):
        for j in range(w):
            if a[i][j] == "#":
                p.append((i,j))
                d[i][j] = 0
    move = [[-1,0],[1,0],[0,-1],[0,1]]
    while p:
        y,x = p.popleft()
        for dy,dx in move:
            y2 = y+dy
            x2 = x+dx
            if 0 <= y2 < h and 0 <= x2 < w:
                if d[y2][x2] < 0:
                    d[y2][x2] = d[y][x]+1
                    p.append([y2,x2])
    ans = 0
    for i in d:
        for j in i:
            if j > ans:
                ans = j
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
    def dijkstra(s):
        d = [float("inf") for i in range(n)]
        d[s] = 0
        q=[[0,s]]
        while q:
            dx,x = heappop(q)
            for y in v[x]:
                if dx+1 < d[y]:
                    d[y] = dx+1
                    heappush(q,[d[y],y])
        return d
    n = I()
    v = [[] for i in range(n)]
    for i in range(n-1):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
    d = dijkstra(0)
    l = d.index(max(d))
    d = dijkstra(l)
    m = max(d)+1
    if m%3 == 2:
        print("Second")
    else:
        print("First")
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
    A()
