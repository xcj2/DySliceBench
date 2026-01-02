from math import sqrt

class UF():
  def __init__(self, N):
    self.parents = [-1] * (N+1)

  def find(self, n):
    if self.parents[n] < 0:
      return n
    else:
      self.parents[n] = self.find(self.parents[n])
      return self.parents[n]

  def union(self, u,v):
    p1,p2 = self.find(u),self.find(v)
    if p1 == p2: return

    if p1 > p2:
      p1,p2 = p2,p1
    self.parents[p1] += self.parents[p2]
    self.parents[p2] = p1

  def same(self, u, v):
    return self.find(u) == self.find(v)

ans = []
while True:
  # sphere-shaped
  n = int(input())
  if n==0: exit()
  C = []
  # for _ in range(n):
    # C.append(list(map(float,input().split())))
  C = [[float(i) for i in input().split()] for _ in range(n)]

  uf = UF(n)
  edges = []
  for i in range(n):
    for j in range(i+1, n):
      x1,y1,z1,r1 = C[i]
      x2,y2,z2,r2 = C[j]
      d = ((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**0.5-r1-r2
      if d <= 0:
        uf.union(i,j)
      else:
        edges.append((d,i,j))
  edges.sort(key=lambda x: x[0])

  res = 0
  for d,u,v in edges:
    if not uf.same(u,v):
      uf.union(u,v)
      res += d

  print(f"{res:.3f}")
