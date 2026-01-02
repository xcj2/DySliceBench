class UnionFind:
  def __init__(self):
    self.ht = {}

  def same(self, x, y):
    x = self.ht[x]
    y = self.ht[y]
    return x.root() == y.root()

  def unite(self, x, y):
    nx = self.ht[x]
    ny = self.ht[y]
    if self.same(x, y):
      return
    xr = nx.root()
    yr = ny.root()
    xr.set_parent(yr)

  def add(self, x):
    n = Node(x)
    n.set_parent(None)
    self.ht[x] = n

  def show(self):
    roots = {}
    for n in self.ht.values():
      nr = n.root()
      if nr in roots:
        roots[nr].append(n.val)
      else:
        roots[nr] = [n.val]
    for s in roots.values():
      print(s)

  def get_set(self):
    roots = {}
    for n in self.ht.values():
      nr = n.root()
      if nr in roots:
        roots[nr].append(n.val)
      else:
        roots[nr] = [n.val]
    return roots.values()

class Node:
  def __init__(self, val):
    self.val = val

  def root(self):
    n = self
    chain = []
    while n.parent != None:
      chain.append(n)
      n = n.parent
    root = n
    for n in chain:
      n.set_parent(root)
    return root

  def set_parent(self, x):
    self.parent = x


## main

n, m = map(int, input().split())
uf = UnionFind()

for i in range(1, n+1):
  uf.add(i)

for _ in range(m):
  x, y, z = map(int, input().split())
  uf.unite(x, y)

cnt = len(uf.get_set())

print(cnt)
