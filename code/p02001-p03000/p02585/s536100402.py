from collections import defaultdict

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
    ret = defaultdict(list)
    for i in range(self.n):
      ret[self.find(i)].append(i)
    return ret

  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

N, K = map(int, input().split())
P = list(map(lambda x: int(x)-1, input().split()))
C = list(map(int, input().split()))

uf = UnionFind(N)

for i in range(N):
  uf.union(i, P[i])

D = uf.all_group_members()
E = defaultdict(list)
F = defaultdict(int)

Num = [0]*N

for root in uf.roots():
  i = root
  n = 0
  E[root].append(0)
  while P[i] != root:
    i = P[i]
    n += 1
    Num[i] = n
    E[root].append(E[root][-1] + C[i])
  E[root].append(E[root][-1] + C[root])
  F[root] = n + 1
  i = root
  while P[i] != root:
    i = P[i]
    E[root].append(E[root][-1] + C[i])
  E[root].append(E[root][-1] + C[root])

#print(Num, E, F, sep="\n")
ans = -float("inf")

for root, L in E.items():
  loop, k = divmod(K, F[root])
  if k == 0:
    loop -= 1
    k += F[root]
  temp = 0
  if L[-1] >= 0:
    temp += (L[-1]//2) * loop
  else:
    if loop >= 1:
      k = F[root]
  for i in range(F[root]):
    for j in range(i+1, i+k+1):
      ans = max(ans, temp + E[root][j] - E[root][i])

print(ans)