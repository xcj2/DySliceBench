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
    n,h,w = IR(3)
    print((n-h+1)*(n-w+1))
    return

#B
def B():
    n = I()
    a,b = LI()
    p = LI()
    k = [0 for i in range(a+1)]
    k += [1 for i in range(b-a)]
    k += [2 for i in range(max(p)+1-b)]
    d = defaultdict(int)
    for i in p:
        d[k[i]] += 1
    ans = min(d[0],d[1],d[2])
    print(ans)
    return

#C
def C():
    h,w = LI()
    s = SR(h)
    bfs_map = [[-1 for i in range(w)] for j in range(h)]
    d = [[0,1],[0,-1],[1,0],[-1,0]]
    ans = 0
    for y in range(h):
        for x in range(w):
            if s[y][x] == "#":
                if bfs_map[y][x] < 0:
                    bfs_map[y][x] = 0
                    a = 1
                    b = 0
                    q = deque()
                    q.append([y,x])
                    while q:
                        n,m = q.popleft()
                        for dy,dx in d:
                            n2 = n+dy
                            m2 = m+dx
                            if 0 <= n2 < h and 0 <= m2 < w:
                                if s[n][m] != s[n2][m2] and bfs_map[n2][m2] < 0:
                                    if s[n2][m2] == "#":a += 1
                                    else:b += 1
                                    bfs_map[n2][m2] = 0
                                    q.append([n2,m2])
                    ans += a*b
    print(ans)
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
    C()
