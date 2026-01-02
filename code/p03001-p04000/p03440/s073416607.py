# -*- coding: utf-8 -*-
from collections import defaultdict
from heapq import merge
import sys
sys.setrecursionlimit(10**7)
def inpl(): return tuple(map(int, input().split()))
 
N, M = inpl()
A = inpl()
tree = [[-1, 1]  for _ in range(N)] # [next, rank]
 
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
  
for _ in range(M):
    x, y = tuple(map(int, input().split()))
    if not int(find(x) == find(y)):
        unite(x, y)
 
D = defaultdict(list)
for n in range(N):
    D[find(n)].append(A[n])
 
H = []
res = 0 

for k, v in D.items():
    v = sorted(v)
    res += v[0]
    H.append(v[1:])
 
if N < 2*(N-M-1):
    print("Impossible")
elif M == N-1:
    print(0)
else:
    res += sum(list(merge(*H))[:2*(N-M-1) - len(D.keys())])
    print(res)