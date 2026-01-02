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
        bfs_map = [1 for i in range(n)]
        bfs_map[0] = 0
        q = deque()
        q.append(0)
        s = 1
        while q:
            x = q.pop()
            for y in v[x]:
                if [x,y] != [a,b] and [x,y] != [b,a]:
                    if bfs_map[y]:
                        bfs_map[y] = 0
                        q.append(y)
                        s += 1
        return s
    n,m = LI()
    v = [deque() for i in range(n)]
    l = deque()
    for i in range(m):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
        l.append([a,b])
    ans = 0
    for a,b in l:
        s = bfs(a,b)
        if s < n:
            ans += 1
    print(ans)
#D
def D():
    n,k = LI()
    v = [None for i in range(n)]
    for i in range(n):
        v[i] = LI()
        v[i] = [[None,None]]+[v[i]]
    v.sort(key = lambda x:x[1][1])
    for i in range(n):
        v[i][0][1] = i
    v.sort(key = lambda x:x[1][0])
    for i in range(n):
        v[i][0][0] = i
    po = [[None for i in range(n)] for j in range(n)]
    h = [None for i in range(n)]
    w = [None for i in range(n)]
    for i in range(n):
        po[v[i][0][0]][v[i][0][1]] = v[i][1]
        h[v[i][0][0]] = v[i][1][0]
        w[v[i][0][1]] = v[i][1][1]
    re = [[[[0 for x in range(n)] for y in range(n)] for t in range(n)] for s in range(n)]
    ans = float("inf")
    for s in range(n):
        for t in range(n):
            for y in range(s,n):
                for x in range(t,n):
                    if x == t:
                        re[s][t][y][x] = re[s][t][y-1][x]
                    else:
                        re[s][t][y][x] = max(0,re[s][t][y][x-1]+re[s][t][y-1][x]-re[s][t][y-1][x-1])
                    if po[y][x] != None:
                        re[s][t][y][x] += 1
                    if re[s][t][y][x] >= k:
                        ans = min(ans,(h[y]-h[s])*(w[x]-w[t]))
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
    D()
