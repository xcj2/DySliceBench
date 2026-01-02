class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            x, y = y, x
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        self.size[x] += self.size[y]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]


def p_e():
    n, m = map(int, input().split())
    uf = UnionFind(n)
    for _ in range(m):
        x, y, z = map(int, input().split())
        uf.unite(x - 1, y - 1)
    ans = set()
    for i in range(n):
        ans.add(uf.find(i))
    print(len(ans))
    

if __name__ == '__main__':
    p_e()