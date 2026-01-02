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

ans=[uf.size(i)-len(tree_f[i])-len(tree_g[i])-1 for i in range(1,n+1)]
print(*ans)