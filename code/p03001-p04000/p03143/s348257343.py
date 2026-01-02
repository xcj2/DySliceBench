import sys
input = sys.stdin.readline

class UnionFind():
    def __init__(self, X):
        self.n = len(X)
        self.parents = [-x for x in X]

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
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
      
n, m = map(int, input().split())
X = [0] + list(map(int, input().split()))
edge = []
for _ in range(m):
  a, b, y = map(int, input().split())
  edge.append((y, a, b))
edge.sort()
G = [[] for _ in range(n+1)]
for y, a, b in edge:
  G[a].append((b, y))
  G[b].append((a, y))
uf = UnionFind(X)
T = []
for y, a, b in edge:
  uf.unite(a, b)
  if uf.size(a) >= y:
    T.append(1)
  else:
    T.append(0)
seen = [False]*(n+1)
used = set()
cnt = 0

def dfs(e):
  y, a, b = edge[e]
  res = 0
  seen[a] = True
  stack = [a]
  while stack:
    v = stack.pop()
    for nv, cost in G[v]:
      if cost > y:
        continue
      if (v, nv) in used:
        continue
      res += 1
      used.add((v, nv))
      used.add((nv, v))
      if seen[nv]:
        continue
      stack.append(nv)
      seen[nv] = True
  return res
for i in range(m-1, -1, -1):
  if T[i] and not seen[edge[i][1]]:
    cnt += dfs(i)
ans = m - cnt
print(ans)