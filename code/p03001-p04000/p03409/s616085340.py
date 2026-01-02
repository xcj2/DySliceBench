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
    def bfs(a,b):
        bfs_map = [-1 for i in range(2*n+2)]
        q = [a]
        bfs_map[a] = 0
        while q:
            x = q.pop(0)
            for y in out[x]:
                if bfs_map[y] == -1:
                    q.append(y)
                    bfs_map[y] = bfs_map[x]+1
        if bfs_map[b] == -1:return 0
        d = bfs_map[b]
        path = [b]
        y = b
        while d > 0:
            for x in ent[y]:
                if bfs_map[x] == d-1:
                    path.insert(0,x)
                    y = x
                    d -= 1
                    break
        return path

    def ford_fulkerson(a,b,c):
        ans = 0
        while 1:
            path = bfs(a,b)
            if not path:break
            for i in range(len(path)-1):
                out[path[i]].remove(path[i+1])
                ent[path[i+1]].remove(path[i])
                if not c[path[i+1]][path[i]]:
                    c[path[i+1]][path[i]] = 1
                    out[path[i+1]].append(path[i])
                    ent[path[i]].append(path[i+1])
            ans += 1
        return ans
    n = I()
    r = LIR(n)
    b = LIR(n)
    c = [[0 for i in range(2*n+2)] for i in range(2*n+2)]
    out = [[] for i in range(2*n+2)]
    ent = [[] for i in range(2*n+2)]
    for i in range(n):
        c[0][i+1] = 1
        out[0].append(i+1)
        ent[i+1].append(0)
        for j in range(n):
            if r[i][0] < b[j][0] and r[i][1] < b[j][1]:
                c[i+1][n+j+1] = 1
                out[i+1].append(n+j+1)
                ent[n+j+1].append(i+1)
    for j in range(n):
        c[n+j+1][2*n+1] = 1
        out[n+j+1].append(2*n+1)
        ent[2*n+1].append(n+j+1)
    print(ford_fulkerson(0,2*n+1,c))
#D
def D():
    n = I()
    a = LI()
    b = LI()
    s = 0
    for i in range(n):
        s ^= b[i]
    ans = 0
    print(s)
    for i in range(n):
        s ^= a[i]
    print(s)

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
