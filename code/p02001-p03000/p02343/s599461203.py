
class UnionFindTree:

    def __init__(self):
        self.cnt = []
        self.par = []

    def add(self, n):
        assert n == len(self.par), "Invalid Value"
        self.par.append(n)
        self.cnt.append(1)

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            cnt = self.cnt[x] + self.cnt[y]
            self.cnt[x] = cnt
            self.cnt[y] = cnt
            if x < y:
                self.par[y] = x
            else:
                self.par[x] = y

    def size(self, x):
        x = self.root(x)
        return self.cnt[x]


def main():
    n, q = map(int, input().split())
    uf = UnionFindTree()
    for i in range(n):
        uf.add(i)
    for _ in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            uf.unite(x, y)
        else:
            print(1 if uf.same(x, y) else 0)


if __name__ == '__main__':
    main()

