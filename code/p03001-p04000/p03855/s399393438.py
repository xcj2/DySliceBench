from collections import Counter

class Union_Find:

    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.height = [0 for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def getsize(self, x):
        return self.size[self.find(x)]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.height[x] < self.height[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = self.par[x]
            self.size[x] += self.size[y]
            if self.height[x] == self.height[x]:
                self.height[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

N, K, L = map(int, input().split())
uf0 = Union_Find(N+1)
for i in range(K):
    x, y = map(int, input().split())
    uf0.union(x, y)
uf1 = Union_Find(N+1)
for i in range(L):
    x, y = map(int, input().split())
    uf1.union(x, y)
types = [None] * (N+1)
for i in range(1, N+1):
    types[i] = (uf0.find(i), uf1.find(i))
C = Counter(types)
ans = [None] * (N+1)
for i in range(1, N+1):
    ans[i] = C[types[i]]
print(*ans[1:])
