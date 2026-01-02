class UnionFindNode(object):
    def __init__(self, u):
        self.p = u
        self.rank = 0
        self.size = 1


class UnionFind(object):
    def __init__(self, n):
        self.table = [UnionFindNode(i) for i in range(n)]

    def unite(self, u, v):
        self.link(self.find_set(u), self.find_set(v))

    def link(self, u, v):
        if self.table[u].rank > self.table[v].rank:
            self.table[v].p = u
            self.table[u].size += self.table[v].size
        else:
            self.table[u].p = v
            self.table[v].size += self.table[u].size
            if self.table[u].rank == self.table[v].rank:
                self.table[v].rank += 1

    def find_set(self, u):
        if self.table[u].p != u:
            self.table[u].p = self.find_set(self.table[u].p)
        return self.table[u].p

    def size(self, u):
        return self.table[self.find_set(u)].size


n, m = map(int, input().split())
edges = []
for i in range(m):
    ai, bi = map(int, input().split())
    edges.append((ai-1, bi-1))
edges.reverse()

ans = [n * (n - 1) / 2]
uf = UnionFind(n)
for i in range(m-1):
    ai, bi = edges[i]
    if uf.find_set(ai) == uf.find_set(bi):
        ans.append(ans[i])
    else:
        ans.append(ans[i] - uf.size(ai) * uf.size(bi))
        uf.unite(ai, bi)
ans = list(map(int, ans))
ans.reverse()

for x in ans:
    print(x)