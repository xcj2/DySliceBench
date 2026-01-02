f = lambda: map(int,input().split())


class UnionFind(object):
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


n,m = f()
p = list(f())

u = UnionFind(n)
for _ in range(m):
    x,y = f()
    u.unite(x-1, y-1)

gnum = [set() for _ in range(n)]
pnum = [set() for _ in range(n)]
for i in range(n):
    root = u.find(i)
    gnum[root].add(i)
    pnum[root].add(p[i]-1)
ans = 0
for i in range(n):
    ans += len(gnum[i]&pnum[i])
print(ans)
