from collections import defaultdict

N, M, K = map(int, input().split())
F = [tuple(map(lambda s: int(s) - 1, input().split())) for i in range(M)]
B = [tuple(map(lambda s: int(s) - 1, input().split())) for i in range(K)]


class DisjointSet():
    def __init__(self, n):
        self.root = [-1] * n

    def find(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.root[x] > self.root[y]:
            x, y = y, x
        self.root[x] += self.root[y]
        self.root[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.root[self.find(x)]


d = DisjointSet(N)
friends = defaultdict(int)
for Ai, Bi in F:
    d.unite(Ai, Bi)
    friends[Ai] += 1
    friends[Bi] += 1
blocking = defaultdict(list)
for Ci, Di in B:
    blocking[Ci].append(Di)
    blocking[Di].append(Ci)

ans = [0] * N
for i in range(N):
    ans[i] = d.size(i) - friends[i] - 1
    for b in blocking[i]:
        if d.same(i, b):
            ans[i] -= 1
print(' '.join(list(map(str, ans))))
