from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rnk = [0] * (n + 1)

    def find_root(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1

    def isSameGroup(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def size(self, x):
        return -self.root[self.find_root(x)]


N, K, L = map(int, input().split())
UFc = UnionFind(N)
UFt = UnionFind(N)
for _ in range(K):
    p, q = map(int, input().split())
    UFc.unite(p, q)
for _ in range(L):
    p, q = map(int, input().split())
    UFt.unite(p, q)

gr = [0] * (N + 1)
cnt = defaultdict(int)
for i in range(1, N + 1):
    gr[i] = UFc.find_root(i) * (N + 1) + UFt.find_root(i)
    cnt[gr[i]] += 1

ans = [0] * N
for i in range(1, N + 1):
    ans[i-1] = cnt[gr[i]]

print(*ans)
