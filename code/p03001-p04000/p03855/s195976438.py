from collections import defaultdict, Counter
class UF():
  def __init__(self, N):
    self.parents = [-1] * (N+1)

  def union(self, f, t):
    p1 = self.find(f)
    p2 = self.find(t)
    if p1 == p2:
      return

    if self.parents[p1] > self.parents[p2]:
      p1,p2 = p2,p1
    self.parents[p1] += self.parents[p2]
    self.parents[p2] = p1

  def find(self, node):
    if self.parents[node] < 0:
      return node
    else:
      self.parents[node] = self.find(self.parents[node])
      return self.parents[node]

  # def members(self, n):
  #   root = self.find(n)
  #   if root == -1:
  #     return []
  #   import pdb; pdb.set_trace()
  #   return [ i for i, p in enumerate(self.parents) if self.find(i) == root]

N,K,L = map(int, input().split())
uf_road = UF(N)
uf_railway = UF(N)

for _ in range(K):
  f,t = map(int, input().split())
  uf_road.union(f,t)

for _ in range(L):
  f,t = map(int, input().split())
  uf_railway.union(f,t)

l = []
for i in range(1, N+1):
  l.append((uf_road.find(i), uf_railway.find(i)))

c = Counter(l)
for i in range(N):
  print(c[l[i]], end=" ")
