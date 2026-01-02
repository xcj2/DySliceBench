import sys;input=sys.stdin.readline
from heapq import *
def dijkstra(s,cost):
    d = [float("inf")] * NN
    used = [False] * NN
    d[s] = 0
    while True:
        v = -1
        for i in range(NN):
            if (not used[i]) and (v == -1):
                v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
            return d
        used[v] = True
        for j, c in cost[v]:
            d[j] = min(d[j],d[v]+c)

def dijkstra_heapq(s, cost):
    d = [float("inf")] * NN
    h = [(0, s)]
    d[s] = 0
    while h:
        vc, v = heappop(h)
#        print(h)
        if vc > d[v]:
            continue
        for j, c in cost[v]:
            if vc+c<d[j]:
                d[j] = vc+c
                heappush(h, (vc+c, j))
    return d

N,W,S = map(int,input().split())
V = 2500
NN = N*(V+1)

def enc(u, v):
    return u*NN + v

#print(NN)
cost = [[] for _ in range(NN)]
for i in range(W):
    x,y,z,u = map(int,input().split())
    x -= 1
    y -= 1
    for v in range(V+1):
        if v-z>=0:
            cost[x*(V+1)+v].append((y*(V+1)+v-z, u))
            cost[y*(V+1)+v].append((x*(V+1)+v-z, u))

for i in range(N):
    x, y = map(int, input().split())
    for v in range(V+1):
        cost[i*(V+1)+v].append((i*(V+1)+min(v+x, V), y))

S = min(V, S)
d = dijkstra_heapq(S,cost)
for i in range(1, N):
    print(min(d[i*(V+1):(i+1)*(V+1)]))
