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
    if depth == 0:
      return v
    if n<depth:
      return self.root
    ret = v
    for i in range(self.bitn):
      if depth&1<<i:
        ret = self.ancestor_ls[i][ret]
    return ret
  
  def LCA(self,u,v):
    if self.distance[u]<self.distance[v]:
      u,v = v,u
    dif = self.distance[u]-self.distance[v]
    w = self.ancestor(u,dif)
    if w == v:
      return v
    for i in range(self.bitn,-1,-1):
      if self.ancestor_ls[i][w] != self.ancestor_ls[i][v]:
        w,v = self.ancestor_ls[i][w],self.ancestor_ls[i][v]
    return self.ancestor_ls[0][v]

import sys
input = sys.stdin.readline
n = int(input())
ab = [list(map(int,input().split())) for i in range(n-1)]
graph = [[] for i in range(n+1)]
for a,b in ab:
  graph[a].append(b)
  graph[b].append(a)

sol = Doubling(graph,1)
pls = sol.parent()

m = int(input())
cons = [0 for i in range(m)]
for i in range(m):
  u,v = map(int,input().split())
  lca = sol.LCA(u,v)
  while u != lca:
    cons[i] |= 1<<u
    u = pls[u]
  while v != lca:
    cons[i] |= 1<<v
    v = pls[v]
ans = 0
for i in range(2**m):
  x = 0
  for j in range(m):
    if i & 1<<j:
      x |= cons[j]
  bcnt = 0
  for j in range(n+1):
    if x & 1<<j:
      bcnt += 1
  if bin(i).count("1")%2 == 1:
    ans -= 2**(n-1-bcnt)
  else:
    ans += 2**(n-1-bcnt)
print(ans)