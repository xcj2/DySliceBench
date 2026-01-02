class UnionFind:
    def __init__(self, n):
        self._tree = [i for i in range(n)]
        self._rank = [1] * n
    def root(self, a):
        if self._tree[a] == a:return a
        self._tree[a] = self.root(self._tree[a])
        return self._tree[a]
    def is_same_set(self, a, b):
        return self.root(a)==self.root(b)
    def unite(self, a, b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb: return
        if self._rank[ra] < self._rank[rb]:
            self._tree[ra] = rb
        else:
            self._tree[rb] = ra
            if self._rank[ra] == self._rank[rb]:
                self._rank[ra] += 1
I=lambda:map(int,input().split())
N,M=I()
edges=[list(I()) for _ in range(M)]
r=0
for i in range(M):
  uf=UnionFind(N)
  for j in range(M):
    if j!=i: uf.unite(edges[j][0]-1, edges[j][1]-1)
  s={uf.root(n) for n in range(N)}
  if len(s)>1:r+=1
print(r)