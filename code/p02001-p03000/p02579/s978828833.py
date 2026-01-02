import sys
import heapq
INF=10**9
def Dijkstra(graph, start):
  dist={}
  for i in graph:
    dist[i]=INF
  queue=[(0, start)]
  while queue:
    path_len, v=heapq.heappop(queue)
    if dist[v]==INF: 
      dist[v]=path_len
      for w in graph[v]:
        if dist[w]==INF:
          heapq.heappush(queue, (dist[v]+1, w))         
  return dist
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

h,w=map(int,input().split())
ch,cw=map(int,input().split())
dh,dw=map(int,input().split())
m=[]
for i in range(h):
  s=input()
  m.append(s)
uf=UnionFind(h*w)
for i in range(h):
  for j in range(w):
    if j+1<w and m[i][j]=='.' and m[i][j+1]=='.':
      uf.union(i+h*j,i+h*(j+1))
    if i+1<h and m[i][j]=='.' and m[i+1][j]=='.':
      uf.union(i+h*j,i+1+h*j)
if uf.same((ch-1)+(cw-1)*h,(dh-1)+(dw-1)*h):
  print(0)
  sys.exit()
graph={}
for i in uf.roots():
  graph[i]=set()
for i in range(h):
  for j in range(w):
    if m[i][j]!='.':
      continue
    for k in range(-2,3):
      for l in range(3):
        if i+k<0 or i+k>=h or j+l>=w:
          continue
        if m[i+k][j+l]!='.' or uf.same(i+k+(j+l)*h,i+j*h):
          continue
        graph[uf.find(i+k+(j+l)*h)].add(uf.find(i+j*h))
        graph[uf.find(i+j*h)].add(uf.find(i+k+(j+l)*h))
dist=Dijkstra(graph,uf.find(ch-1+(cw-1)*h))
if dist[uf.find(dh-1+(dw-1)*h)]==INF:
  print(-1)
else:
  print(dist[uf.find(dh-1+(dw-1)*h)])