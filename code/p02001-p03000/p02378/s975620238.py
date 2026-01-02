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

# 1:shortest path
# 1_A
"""
from heapq import heappush, heappop
def dijkstra(num, start):
    dist = [float("inf") for i in range(num)]
    dist[start] = 0
    q = [[dist[start], start]]
    while q:
        du, u = heappop(q)
        for j, k in adj[u]:
            if dist[j] > du + k:
                dist[j] = du + k
                heappush(q, [dist[j], j])
                print(dist, q)
    return dist

v,e,r = map(int, input().split(" "))
adj = [[] for i in range(v)]
for i in range(e):
    s,t,d = map(int, input().split(" "))
    adj[s].append([t, d])
lis = dijkstra(v, r)
print(lis)
for i in lis:
    print(str(i).upper())
"""

# 1_B
"""
def bellman_ford(num, start):
    dist = [float("inf") for i in range(num)]
    dist[start] = 0
    for i in range(num):
        update = False
        for j, k, l in adj:
                if dist[k] > dist[j] + l:
                    dist[k] = dist[j] + l
                    update = True
                    if i == num-1:
                        return False
        if not update:
            break
    return dist

v,e,r = map(int, input().split(" "))
adj = []
for i in range(e):
    s,t,d = map(int, input().split(" "))
    adj.append([s, t, d])
lis = bellman_ford(v, r)
if not lis:
    print("NEGATIVE CYCLE")
else:
    for i in lis:
        print(str(i).upper())
"""

# 1_C
"""
def warshallfloyd(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                d[j][k] = min(d[j][k], d[j][i]+d[i][k])
v,e = map(int, input().split())
d = [[float("inf") for j in range(v)] for i in range(v)]
for i in range(v):
    d[i][i] = 0
for i in range(e):
    s, t, c = map(int, input().split())
    d[s][t] = c
warshallfloyd(v)
for i in range(v):
    if d[i][i] < 0:
        print("NEGATIVE CYCLE")
        quit()
for i in d:
    for j in range(v):
        if j < v-1:
            print(str(i[j]).upper(), end = " ")
        else:
            print(str(i[j]).upper())
"""

# 2:spanning tree
# 2_A
"""
def root(x):
    if par[x] == x:
        return x
    par[x] = root(par[x])
    return par[x]

def same(x,y):
    return root(x) == root(y)

def unite(x,y):
    x = root(x)
    y = root(y)
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
v,e = LI()
c = LIR(e)
c.sort(key = lambda x:x[2])
par = [i for i in range(v)]
rank = [0 for i in range(v)]
k = 0
ans = 0
for a,b,w in c:
    if not same(a,b):
        k += 1
        unite(a,b)
        ans += w
    if k == v-1:
        break
print(ans)
"""

#2_B
"""
def root(x):
    if par[x] == x:
        return x
    par[x] = root(par[x])
    return par[x]

def same(x,y):
    return root(x) == root(y)

def unite(x,y):
    x = root(x)
    y = root(y)
    if rank(x) < rank(y):
        par[x] = y
    else:
        par[y] = x
        if rank(x) == rank(y):
            rank[x] += 1
"""

#3:connected components
#3_A

#3_B

#3_C


#4:path/cycle
#4_A
"""
def bellman_ford(num, start):
    dist = [float("inf") for i in range(num)]
    dist[start] = 0
    for i in range(num):
        update = False
        for j, k, l in adj:
            if dist[k] > dist[j] + l:
                dist[k] = dist[j] + l
                update = True
                if i == num-1:
                    return False
        if not update:
            break
    return True

v, e = map(int, input().split(" "))
adj = []
for i in range(e):
    s,t = map(int, input().split(" "))
    adj.append([s, t, -1])
for i in range(v):
    if not bellman_ford(v,i):
        print(1)
        quit()
print(0)
"""

#4_B


#5:tree
#5_A
"""
from heapq import heappush, heappop
def dijkstra(num, start):
    dist = [float("inf") for i in range(num)]
    dist[start]  = 0
    q = [[dist[start], start]]
    while q:
        du, u = heappop(q)
        for j, k in adj[u]:
            if dist[j] > du + k:
                dist[j] = du + k
                heappush(q, [dist[j], j])
    return dist

n = II()
adj = [[] for i in range(n)]
for i in range(n-1):
    s,t,w = LI()
    adj[s].append([t, w])
    adj[t].append([s, w])
d = dijkstra(n,0)
i = d.index(max(d))
d2 = dijkstra(n,i)
print(max(d2))
"""

#5_B
"""
from heapq import heappush, heappop
def dijkstra(num, start):
    dist = [float("inf") for i in range(num)]
    dist[start]  = 0
    q = [[dist[start], start]]
    while q:
        du, u = heappop(q)
        for j, k in adj[u]:
            if dist[j] > du + k:
                dist[j] = du + k
                heappush(q, [dist[j], j])
    return dist

n = int(input())
adj = [[] for i in range(n)]
for i in range(n-1):
    s, t, w = map(int, input().split(" "))
    adj[s].append([t, w])
    adj[t].append([s, w])
for i in range(n):
    s = dijkstra(n,i)
    print(max(s))
"""
#5_C

#5_D

#5_E


#6
#6_A_maximum_flow
"""
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

n,e = LI()
c = [[0 for i in range(n)] for j in range(n)]
for i in range(e):
    a,b,w = LI()
    if a != n-1:
        c[a][b] = w
print(ford_fulkerson(0,n-1,c,n))
"""
#6_B


#7
#7_A
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

x,y,e = LI()
c = [[0 for i in range(x+y+2)] for j in range(x+y+2)]
for i in range(x):
    c[0][i+1] = 1
for i in range(y):
    c[x+i+1][x+y+1] = 1
for i in range(e):
    a,b = LI()
    c[a+1][x+b+1] = 1
print(ford_fulkerson(0,x+y+1,c,x+y+2))

