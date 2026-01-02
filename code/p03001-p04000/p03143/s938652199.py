import sys
from collections import Counter
input = sys.stdin.readline
N, M = map(int, input().split())
X = list(map(int, input().split()))
edges = []
e = [[] for _ in range(N + 1)]
for _ in range(M):
  u, v, c = map(int, input().split())
  edges.append((c, u, v))
  e[u].append((v, c))
  e[v].append((u, c))
edges.sort()
table = [0] + X[: ]
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
use = []
emx = [0] * (N + 1)
for i in range(M):
  c, u, v = edges[i]
  if uf.isSameGroup(u, v):
    rt = uf.Find_Root(u)
    emx[rt] = max(emx[rt], c)
    if table[rt] >= emx[rt]: use.append(i)
  else:
    ur = uf.Find_Root(u)
    vr = uf.Find_Root(v)
    uf.Unite(u, v)
    rt = uf.Find_Root(u)
    cmx = max(emx[ur], emx[vr], c)
    emx[rt] = cmx
    if table[ur] + table[vr] >= cmx: use.append(i)
    table[rt] = table[ur] + table[vr]
use.reverse()
vis = [0] * (N + 1)
evis = Counter()
res = M
for i in use:
  mx, s, _ = edges[i]
  if vis[s]: continue
  sta = [s]
  vis[s] = 1
  while len(sta):
    x = sta.pop()
    for y, c in e[x]:
      if c > mx: continue
      if evis[min(x, y) * M + max(x, y)]: continue
      evis[min(x, y) * M + max(x, y)] = 1
      res -= 1
      if vis[y]: continue
      sta.append(y)
      vis[y] = 1
print(res)