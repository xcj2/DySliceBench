# -*- coding: utf-8 -*-
from operator import itemgetter

import sys
sys.setrecursionlimit(10000)

def inpl(): return tuple(map(int, input().split()))

V, E = inpl()
edges = []
graph = [[] for _ in range(V)]  # [target, cost]
total_cost = 0

for _ in range(E):
    edges.append(inpl())

gw = itemgetter(2)
edges = sorted(edges, key = gw)

tree = [[-1, 1]  for _ in range(V)] # [next, rank]

def find(i):
    if tree[i][0] == -1:
        group = i
    else:
        group = find(tree[i][0])    
    return group
 
def unite(x, y):
    px = find(x)
    py = find(y)
     
    if tree[px][1] == tree[py][1]: # rank is same
        tree[py][0] = px
        tree[px][1] += 1
    else:
        if tree[px][1] < tree[py][1]:
            px, py = py, px
        tree[py][0] = px
 
for s, t, w in edges:
    if find(s) != find(t):
        unite(s, t)
        total_cost += w
        graph[s].append([t, w])
        graph[t].append([s, w])

print(total_cost)
    