n, k, l = map(int, input().split())


class UnionFind():
    def __init__(self, n):
        self.tree = [i for i in range(n)]

    def root(self, x):
        if(self.tree[x] == x):
            return x
        self.tree[x] = self.root(self.tree[x])
        return self.tree[x]  # 経路圧縮

    def same(self, x, y):  # xとyが同じ木に属するか
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if(x == y):
            return
        self.tree[x] = y


uf = UnionFind(n)
uf2 = UnionFind(n)

for _ in range(k):
    p, q = map(int, input().split())
    uf.unite(q-1, p-1)
for _ in range(l):
    r, s = map(int, input().split())
    uf2.unite(s-1, r-1)

#table = [[0]*n for _ in range(n)]
table = dict()

for i in range(n):
    #table[uf.root(i)][uf2.root(i)] += 1
    table[(uf.root(i), uf2.root(i))] = table.get(
        (uf.root(i), uf2.root(i)), 0)+1
for i in range(n):
    print(table[(uf.root(i), uf2.root(i))], end=' ')

exit(0)
for i, j in [(uf.root(i), uf2.root(i)) for i in range(n)]:
    table[i][j] += 1
for i, j in [(uf.root(i), uf2.root(i)) for i in range(n)]:
    print(table[i][j], end=' ')


exit(0)
for i in range(n):
    ans = 0
    for j in range(n):
        if uf.same(i, j) and uf2.same(i, j):
            ans += 1
    print(ans, end=' ')
