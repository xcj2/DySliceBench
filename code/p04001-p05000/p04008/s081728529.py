def DFS(graph,root,parent):
  dist = [-1]*(n+1)
  dist[root] = 0
  stack = [root]
  while stack:
    x = stack.pop()
    for y in graph[x]:
      if dist[y] == -1:
        parent[y] = x
        dist[y] = dist[x]+1
        stack.append(y)
  return dist

#親のリスト、頂点v、kが与えられたときに「vのk個上の祖先」を見る
class Doubling:
  def __init__(self,graph,root):
    self.root = root
    n = len(graph)-1
    self.ancestor_ls = [[0]*(n+1)]
    self.distance = DFS(graph,root,self.ancestor_ls[0])
    self.bitn = n.bit_length()
    for i in range(1,self.bitn+1):
      ancestor_ls_app = [0]*(n+1)
      for j in range(1,n+1):
        ancestor_ls_app[j] = self.ancestor_ls[i-1][self.ancestor_ls[i-1][j]]
      self.ancestor_ls.append(ancestor_ls_app)
  
  def dist(self):
    return self.distance
  
  def parent(self):
    return self.ancestor_ls[0]

  def ancestor(self,v,depth):
    if depth == 1:
      return self.ancestor_ls[0][v]
    if depth == 2:
      return self.ancestor_ls[1][v]
    if depth == 0:
      return v
    if n<depth:
      return self.root
    ret = v
    for i in range(self.bitn):
      if depth&1<<i:
        ret = self.ancestor_ls[i][ret]
    return ret

import sys
input = sys.stdin.readline
from collections import deque
n,k = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
if a[0] != 1:
  ans += 1
graph = [[] for i in range(n+1)]
for i in range(1,n):
  graph[a[i]].append(i+1)
  graph[i+1].append(a[i])
if k > n:
  print(ans)
  exit()
sol = Doubling(graph,1)
dist = sol.dist()
if k == 1:
  print(n-dist.count(1)-dist.count(0)+ans)
  exit()
dls = []
for i in range(1,n+1):
  dls.append((dist[i],i))
vis = [0]*(n+1)
dls.sort()
dlsq = deque(dls)
parent = sol.parent()
while True:
  d,x = dlsq.pop()
  if d <= k:
    break
  if vis[x] == 1:
    continue
  ans += 1
  anc = sol.ancestor(x,k-1)
  stack = deque([anc])
  while stack:
    v = stack.pop()
    vis[v] = 1
    for u in graph[v]:
      if parent[u] == v and vis[u] != 1:
        stack.append(u)
print(ans)