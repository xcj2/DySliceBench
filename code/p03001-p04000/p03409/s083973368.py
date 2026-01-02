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
    return

#B
def B():
    return

#C
def C():
    def bfs(s,g,n):
        bfs_map = [-1 for i in range(n)]
        bfs_map[s] = 0
        q = deque()
        q.append(s)
        fin = False
        while q:
            x = q.popleft()
            for y in range(n):
                if c[x][y] > 0 and bfs_map[y] < 0:
                    bfs_map[y] = bfs_map[x]+1
                    if y == g:
                        fin = True
                        break
                    q.append(y)
            if fin:
                break

        if bfs_map[g] == -1:
            return [None,0]
        path = [None for i in range(bfs_map[g]+1)]
        m = float("inf")
        path[bfs_map[g]] = g
        y = g
        for i in range(bfs_map[g])[::-1]:
            for x in range(n+1):
                if c[x][y] > 0 and bfs_map[x] == bfs_map[y]-1:
                    path[i] = x
                    if c[x][y] < m:
                        m = c[x][y]
                    y = x
                    break
        return [path,m]

    def ford_fulkerson(s,g,c,n):
        while 1:
            p,m = bfs(s,g,n)
            if not m:break
            for i in range(len(p)-1):
                c[p[i]][p[i+1]] -= m
                c[p[i+1]][p[i]] += m
        return sum(c[g])

    n = I()
    r = LIR(n)
    b = LIR(n)
    c = [[0 for i in range(2*n+2)] for i in range(2*n+2)]
    for i in range(n):
        c[0][i+1] = 1
        for j in range(n):
            if r[i][0] < b[j][0] and r[i][1] < b[j][1]:
                c[i+1][n+j+1] = 1
    for j in range(n):
        c[n+j+1][2*n+1] = 1
    print(ford_fulkerson(0,2*n+1,c,2*n+2))
#D
def D():
    n = I()
    a = LI()
    b = LI()
    ans = 0
    p = 1
    for k in range(30):
        s = 0
        c = [b[i]%(p*2) for i in range(n)]
        a_ = [a[i]%(p*2) for i in range(n)]
        c.sort()
        a_.sort()
        l1,l2,l3 = 0,0,0
        y = float("inf")
        for x in a_[::-1]:
            if x != y:
                while l1 < n and c[l1] < p-x:l1 += 1
                while l2 < n and c[l2] < 2*p-x:l2 += 1
                while l3 < n and c[l3] < 3*p-x:l3 += 1
            s += n-l2-l1-l3
            y = x
        ans += (s%2)*p
        p *= 2
    print(ans)
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
