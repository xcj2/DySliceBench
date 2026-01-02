from collections import defaultdict

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
    


N,M,K = map(int, input().split())
uf = UnionFind(N)
friend = defaultdict(int)
block = defaultdict(int)

for _ in range(M):
    a,b = map(int, input().split())
    friend[a-1] += 1
    friend[b-1] += 1
    uf.union(a-1,b-1)

for _ in range(K):
    a,b = map(int, input().split())
    if uf.same(a-1,b-1):
        block[a-1] += 1
        block[b-1] += 1

result = [uf.size(i) - friend[i] - block[i] - 1 for i in range(N)]
print(' '.join(map(str, result)))