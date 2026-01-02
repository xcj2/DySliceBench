from collections import Counter


def same_group():
    class UnionFind(object):
        def __init__(self, n):
            self.par = [i for i in range(n)]
            self.rank = [0 for _ in range(n)]

        def find(self, x):
            if self.par[x] != x:
                self.par[x] = self.find(self.par[x])
            return self.par[x]

        def unite(self, x, y):
            x = self.find(x)
            y = self.find(y)
            if self.rank[x] < self.rank[y]:
                self.par[x] = y
            else:
                self.par[y] = x
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

        def is_same_group(self, x, y):
            return self.find(x) == self.find(y)

    N, M, K = map(int, input().split())

    uf = UnionFind(N)
    friends = {i: 0 for i in range(N)}
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if uf.find(a) != uf.find(b):
            uf.unite(a, b)

        friends[a] += 1
        friends[b] += 1

    for i in range(N):
        uf.find(i)

    num_per_group = Counter(uf.par)

    blocks = {i: 0 for i in range(N)}
    for _ in range(K):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if uf.par[c] == uf.par[d]:
            blocks[c] += 1
            blocks[d] += 1

    print(*[max(num_per_group[uf.par[i]] - friends[i] - blocks[i] - 1, 0) for i in range(N)])


same_group()
