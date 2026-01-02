from collections import defaultdict

class UnionFind:
    def __init__(self, n):
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

    def is_same_root(self, x, y):
        return self.find(x) == self.find(y)

    def get_group_size(self, x):
        return -self.parents[self.find(x)]

N, M, K = map(int, input().split())
uf = UnionFind(N)

friends = defaultdict(set)
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    friends[u].add(v)
    friends[v].add(u)
    uf.union(u, v)
blocks = [0]*N
for _ in range(K):
    u, v = map(lambda x: int(x)-1, input().split())
    if uf.is_same_root(u, v):
        blocks[u] += 1
        blocks[v] += 1

res = [uf.get_group_size(i)-len(friends[i])-blocks[i]-1 for i in range(N)]
print(' '.join(map(str, res)))
