#!usr/bin/env python3
from collections import defaultdict
import math
import bisect
def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()
def IIR(n): return [II() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
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
#6_A

#6_B


#7
#7_A

