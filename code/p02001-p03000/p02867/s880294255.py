import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
xa = sorted([(a[i], i) for i in range(N)], key = lambda x: x[0])
xb = sorted([(b[i], i) for i in range(N)], key = lambda x: x[0])
for i in range(N):
  if xa[i][0] > xb[i][0]:
    print("No")
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
c = 0
#print(xa, xb)
f = 0
for i in range(N):
  #print((xa[i][1], xb[i][1]))
  if uf.isSameGroup(xa[i][1], xb[i][1]):
    c += 1
  uf.Unite(xa[i][1], xb[i][1])
if c >= 2:
  print("Yes")
else:
  for i in range(N - 1):
    if xa[i + 1] <= xb[i]:
      print("Yes")
      exit(0)
  print("No")