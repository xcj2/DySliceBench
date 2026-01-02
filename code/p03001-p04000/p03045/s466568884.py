class UnionFind:
    def __init__(self, N):
        # par = parent
        self.par = [i for i in range(N)]
        return

    def root(self, x):
        if self.par[x] == x:
            return (x)
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def same(self, x, y):
        return (self.root(x) == self.root(y))

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if (x == y):
            return False

        self.par[x] = min(x, y)
        self.par[y] = min(x, y)
        return True


def inpl():
    return list(map(int, input().split()))


N, M = inpl()
uf = UnionFind(N)
for i in range(M):
    x, y, z = inpl()
    x -= 1
    y -= 1
    uf.union(x, y)

ans = []
for i in range(N):
    ans.append(uf.root(i))
print(len(set(ans)))
