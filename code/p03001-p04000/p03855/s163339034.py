from collections import defaultdict

class UnionFind:
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

N, K, L = map(int, input().split())

road = UnionFind(N)
railway = UnionFind(N)

for _ in range(K):
    p, q = map(int, input().split())
    road.union(p-1, q-1)

for _ in range(L):
    p, q = map(int, input().split())
    railway.union(p-1, q-1)

counter = defaultdict(int)
for i in range(N):
    counter[(road.find(i), railway.find(i))] += 1
ans = []
for i in range(N):
    ans.append(counter[(road.find(i), railway.find(i))])

print(*ans)
