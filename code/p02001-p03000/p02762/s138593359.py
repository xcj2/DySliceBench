import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M, K = mapint()

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

uf = UnionFind(N)
blocks = set()
friends = [0]*N
possi = [0]*N
for _ in range(M):
    a, b = mapint()
    uf.union(a-1, b-1)
    friends[a-1] += 1
    friends[b-1] += 1
for _ in range(K):
    a, b = mapint()
    if uf.same(a-1, b-1):
        friends[a-1] += 1
        friends[b-1] += 1
for i in range(N):
    possi[i] = uf.size(i)-friends[i]-1
print(*possi)