from sys import stdin
nii=lambda: map(int, stdin.readline().split())

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
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


n,m,k=map(int,input().split())

tree_f=[[] for i in range(n+1)]
tree_g=[[] for i in range(n+1)]

uf=UnionFind(n+1)

for i in range(m):
  a,b=nii()
  tree_f[a].append(b)
  tree_f[b].append(a)
  uf.union(a,b)

for i in range(k):
  a,b=nii()
  if uf.find(a)==uf.find(b):
    tree_g[a].append(b)
    tree_g[b].append(a)

ans=[]
for i in range(n):
  i+=1
#  sst=list(set(tree_f[i]+tree_g[i]) & set(uf.members(i)))
#  cnt=len(sst)
  cnt=len(tree_f[i])+len(tree_g[i])
  ans.append(uf.size(i)-cnt-1)

print(*ans)