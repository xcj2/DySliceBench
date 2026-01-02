import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())
a = list(map(int, input().split()))
res = 0
if M == 0:
  if N == 1:
    print(0)
  elif N == 2:
    print(sum(a))
  else: print("Impossible")
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

uf = UnionFind(N - 1)
for _ in range(M):
  u, v = map(int, input().split())
  uf.Unite(u, v)
hs = [[] for _ in range(N + 1)]
for x in range(N):
  y = uf.Find_Root(x)
  heapq.heappush(hs[y], a[x])
#print(hs)
c = 0
t = []
for x in range(N):
  if len(hs[x]):
    c += 1
    res += heapq.heappop(hs[x])
    t += hs[x]
t.sort()
#print(c, t, hs, res)
if c == 1:
  print(0)
  exit(0)
if len(t) < c - 2:
  print("Impossible")
  exit(0)
for i in range(c - 2):
  if i >= c - 2:
    print("Impossible")
    exit(0)
  res += t[i]
print(res)