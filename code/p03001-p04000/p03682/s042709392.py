class UnionFind(object):
  def __init__(self, n=1):
    self.par = [i for i in range(n)]
    self.rank = [0 for _ in range(n)]
    self.size = [1 for _ in range(n)]
  def find(self, x):
    if self.par[x] == x:
      return x
    else:
      self.par[x] = self.find(self.par[x])
      return self.par[x]
  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x != y:
      if self.rank[x] < self.rank[y]:
        x, y = y, x
      if self.rank[x] == self.rank[y]:
        self.rank[x] += 1
      self.par[y] = x
      self.size[x] += self.size[y]
  def is_same(self, x, y):
    return self.find(x) == self.find(y)
  def get_size(self, x):
    x = self.find(x)
    return self.size[x]

import sys
input = sys.stdin.readline

from heapq import heapify, heappop, heappush

N = int(input())
X = []; Y = []
for i in range(N):
  x,y = map(int,input().split())
  X.append((x,i));Y.append((y,i))
X.sort();Y.sort()
dx = [];dy =[]
for i in range(N-1):
  tx = X[i+1][0]-X[i][0]
  dx.append((tx,(X[i+1][1],X[i][1])))
  ty = Y[i+1][0]-Y[i][0]
  dy.append((ty,(Y[i+1][1],Y[i][1])))
heapify(dx);heapify(dy)
#print(dx,dy)
visited = set([])
ans = 0
uf = UnionFind(N)
while uf.get_size(0) < N:
  if not dy or dx[0] <= dy[0]:
    cost, loc = heappop(dx)
  else:
    cost, loc = heappop(dy)
  if uf.is_same(loc[0],loc[1]): #すでに接続済みのところはスキップ
    continue
  ans += cost
  #print(cost)
  uf.union(loc[0],loc[1])
print(ans)