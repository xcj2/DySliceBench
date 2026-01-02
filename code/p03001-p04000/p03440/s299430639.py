import sys
input = sys.stdin.readline
N, M = map(int, input().split())
a = list(map(int, input().split()))
if N == 1:
  print(0)
  exit(0)
if M == 0 and (N > 2):
  print("Impossible")
  exit(0)
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
d = [[] for _ in range(N)]
for _ in range(M):
  u, v = map(int, input().split())
  uf.Unite(u, v)
for i in range(N):
  d[uf.Find_Root(i)].append(a[i])
res = 0
x = []
y = 0
for i in range(N):
  d[i].sort(reverse = True)
  if len(d[i]):
    res += d[i].pop()
    y += 1
  x += d[i]
if y == 1:
  print(0)
  exit(0)
x.sort()
for i in range((y - 1) * 2 - y):
  if i >= len(x):
    print("Impossible")
    exit(0)
  res += x[i]
print(res)