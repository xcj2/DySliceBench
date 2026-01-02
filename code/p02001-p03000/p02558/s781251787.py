import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
class DisjointSetUnion():
  def __init__(self, n):
    self.n = n
    self.root = [-1] * (n + 1)
    self.rank = [0] * (n + 1)
  def leader(self, x):
    rt = self.root[x]
    if rt < 0: return x
    else: self.root[x] = self.leader(rt)
    return self.root[x]
  def merge(self, x, y):
    leader = self.leader
    xrt = leader(x)
    yrt = leader(y)
    if xrt == yrt: return
    if self.rank[xrt] > self.rank[yrt]:
      self.root[xrt] += self.root[yrt]
      self.root[yrt] = xrt
    else:
      self.root[yrt] += self.root[xrt]
      self.root[xrt] = yrt
      self.rank[yrt] += self.rank[xrt] == self.rank[yrt]
  def same(self, x, y): return self.leader(x) == self.leader(y)
  def size(self, x):  return -self.root[self.leader(x)]
  def group(self):
    n = self.n
    leader = self.leader
    res = [[] for _ in range(n + 1)]
    for x in range(n + 1): res[leader(x)].append(x)
    return [res[i] for i in range(n + 1) if len(res[i])]
dsu = DisjointSetUnion(N)
for _ in range(Q):
  q, u, v = map(int, input().split())
  if q: print(int(dsu.same(u, v)))
  else: dsu.merge(u, v)