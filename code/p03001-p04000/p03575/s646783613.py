f = lambda: list(map(int,input().split()))
f_ = lambda: [int(x)-1 for x in input().split()]


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
E = []
for _ in range(m):
    E.append(f_())

ans = 0
for edge in E:
    e = [i for i in E if not i == edge]
    u = UnionFind(n)
    for a,b in e:
        u.unite(a,b)

    f = False
    k = u.find(0)
    for i in range(n):
        if u.find(i) is not k:
            f = True
            break
    if f:
        ans += 1
print(ans)
