class UnionFind:
    def __init__(self, n=1):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.parent[y] = x
    
    def is_same(self, x, y):
        return self.find(x) == self.find(y)


N, M = map(int, input().split())
A = list(map(int, input().split()))
uf = UnionFind(N)
for i in range(M):
  x, y = map(int, input().split())
  uf.union(x, y)

for i in range(N):
  uf.find(i)

par = [uf.find(i) for i in range(N)]
d = {}
for i, p in enumerate(par):
  if p in d:
    d[p].append(A[i])
  else:
    d[p] = [A[i]]

num = len(d)
if num == 1:
  print(0)
  quit()

a = []
ans = 0
for p in d:
  d[p].sort(reverse=True)
  ans += d[p].pop()
  a += d[p]

a.sort()
n = 2*(N - M - 1) - num
if len(a) < n:
  print('Impossible')
else:
  print(sum(a[:n]) + ans)