import sys
from collections import Counter
input = sys.stdin.readline
N, M = map(int, input().split())
a = list(map(int, input().split()))
e = []
ee = [[] for _ in range(N + 1)]
for _ in range(M):
  u, v, c = map(int, input().split())
  e.append((c, u, v))
  ee[u].append((v, c))
  ee[v].append((u, c))
e.sort()

table = [0] + a[: ]

class UnionFind():
  def __init__(self, n):
    self.n = n
    self.root = [-1] * (n + 1)
    self.rnk = [0] * (n + 1)

  def Find_Root(self, x):
    if self.root[x] < 0:
      return x
    else:
      self.root[x] = self.Find_Root(self.root[x])
      return self.root[x]

  def Unite(self, x, y):
    x = self.Find_Root(x)
    y = self.Find_Root(y)
    if x == y:
      return 
    elif self.rnk[x] > self.rnk[y]:
      self.root[x] += self.root[y]
      self.root[y] = x
    else:
      self.root[y] += self.root[x]
      self.root[x] = y
      if self.rnk[x] == self.rnk[y]:
        self.rnk[y] += 1

  def isSameGroup(self, x, y):
    return self.Find_Root(x) == self.Find_Root(y)

  def Count(self, x):
    return -self.root[self.Find_Root(x)]

uf = UnionFind(N)
edges = []
etable = [0] * (N + 1)
for i in range(M):
  c, u, v = e[i]
  if uf.isSameGroup(u, v):
    rt = uf.Find_Root(u)
    etable[rt] = max(etable[rt], c)
    if table[rt] >= etable[rt]: edges.append(i)

  else:
    ur = uf.Find_Root(u)
    vr = uf.Find_Root(v)
    uf.Unite(u, v)
    rt = uf.Find_Root(u)
    cmx = max(etable[ur], etable[vr], c)
    etable[rt] = cmx
    if table[ur] + table[vr] >= cmx: edges.append(i)

    table[rt] = table[ur] + table[vr]
edges.reverse()
vis = [0] * (N + 1)
evis = Counter()
res = M
#print(edges)
for i in edges:
  mx, s, _ = e[i]
  if vis[s]: continue
  sta = [s]
  vis[s] = 1
  while len(sta):
    x = sta.pop()
    for y, c in ee[x]:
      if c > mx: continue
      if evis[(min(x, y), max(x, y))]: continue
      evis[(min(x, y), max(x, y))] = 1
      res -= 1
      if vis[y]: continue
      sta.append(y)
      vis[y] = 1
  #print(vis, res, e[i])
print(res)