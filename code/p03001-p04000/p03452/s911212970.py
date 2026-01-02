# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10000)
from collections import defaultdict, deque
def inpl(): return tuple(map(int, input().split()))
 
N, M = inpl()
Q = [inpl() for _ in range(M)]
# グループごとにトポロジカルソートをして、最後の方から遡って計算
 
tree = [[-1, 1]  for _ in range(N+1)] # [next, rank]
  
def find(i):
    if tree[i][0] == -1:
        group = i
    else:
        group = find(tree[i][0]) 
        tree[i][0] = group
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
 
adj = [[] for _ in range(N+1)]  
 
for l, r, d in Q:
    if find(l) != find(r):
        unite(l, r)
    adj[l].append([r, d])
    adj[r].append([l, -d])
 
 
G = set([find(n) for n in range(1, N+1)])
 
X = [-1 for _ in range(N+1)]
searched = [False for _ in range(N+1)]
res = True
 
for g in G:
    X[g] = 0
    Q = deque([g])
    searched[g] = True
    while Q:
        p = Q.popleft()
        for np, d in adj[p]:
            if searched[np]:
                if X[np] != X[p] + d:
                    Q = []
                    res = False
                    break
            else:
                X[np] = X[p] + d
                Q.append(np)
                searched[np] = True
    if not res:
        break
 
if res:
    print("Yes")
else:
    print("No")