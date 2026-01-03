# -*- coding: utf-8 -*-
from itertools import combinations
from collections import defaultdict
import sys
sys.setrecursionlimit(10000)
def inpl(): return tuple(map(int, input().split()))
 
N, K, L = inpl()
 
tree = [[[-1, 1]  for _ in range(N+1)] for _ in range(2)] # [next, rank]

def find(i, t):
    if tree[t][i][0] == -1:
        group = i
    else:
        group = find(tree[t][i][0], t)
        tree[t][i][0] = group
    return group
 
def unite(x, y, t):
    px = find(x, t)
    py = find(y, t)
     
    if tree[t][px][1] == tree[t][py][1]: # rank is same
        tree[t][py][0] = px
        tree[t][px][1] += 1
    else:
        if tree[t][px][1] < tree[t][py][1]:
            px, py = py, px
        tree[t][py][0] = px
 
for _ in range(K):
    x, y = inpl()
    if not int(find(x, 0) == find(y, 0)):
        unite(x, y, 0)

for _ in range(L):
    x, y = inpl()
    if not int(find(x, 1) == find(y, 1)):
        unite(x, y, 1)

D = defaultdict(lambda: 0)
P = []
for i in range(1, N+1):
    a, b = find(i, 0), find(i, 1)
    D[(a, b)] += 1
    P.append((a, b))
print(" ".join(map(str, [D[(a, b)] for a, b in P])))