n, m = map(int, input().split())
lrd = [list(map(int, input().split())) for _ in range(m)]


class WeightedUnionFind:
    def __init__(self, x):
        self.p = [e for e in range(x)]
        self.rank = [0] * x
        self.weight = [0] * x

    def same(self, u, v):
        return self.find_set(u) == self.find_set(v)

    def find_set(self, u):
        if u != self.p[u]:
            v = self.find_set(self.p[u])
            self.weight[u] += self.weight[self.p[u]]
            self.p[u] = v

        return self.p[u]

    def unite(self, u, v, w):
        w += self.weight[u]
        w -= self.weight[v]

        u = self.find_set(u)
        v = self.find_set(v)

        if self.rank[u] < self.rank[v]:
            u, v = v, u
            w = -w

        if self.rank[u] == self.rank[v]:
            self.rank[u] += 1

        self.p[v] = u

        self.weight[v] = w

    def get_weight(self, u):
        self.find_set(u)
        return self.weight[u]

    def diff(self, u, v):
        return self.get_weight(v) - self.get_weight(u)


wuf = WeightedUnionFind(n)

for l, r, d in lrd:
    l -= 1
    r -= 1

    if wuf.same(l, r):
        #print(l, r, d, wuf.diff(l, r), wuf.weight)
        if wuf.diff(l, r) != d:
            print("No")
            exit()

    else:
        wuf.unite(l, r, d)

print("Yes")
