

class UnionFind:

    def __init__(self, n):
        self.p = {i: i for i in range(n)}
        self.r = {i: 0 for i in range(n)}

    def root(self, x):
        if self.p[x] == x:
            return x
        self.p[x] = self.root(self.p[x])
        return self.p[x]

    def merge(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.r[x] < self.r[y]:
            self.p[x] = y
        else:
            self.p[y] = x
            if self.r[x] == self.r[y]:
                self.r[x] += 1

    def cluster(self):
        c = {}
        for x in self.p:
            xx = self.root(x)
            if xx not in c:
                c[xx] = {x}
            else:
                c[xx].add(x)
        return c


def main():
    n, m = list(map(int, input().split()))
    pp = list(map(int, input().split()))
    uf = UnionFind(n)
    for _ in range(m):
        x, y = map(int, input().split())
        uf.merge(x - 1, y - 1)
    cc = uf.cluster()
    count = 0
    for clt in cc.values():
        p = set(pp[i] - 1 for i in clt)
        count += len(p & clt)
    print(count)


if __name__ == '__main__':
    main()
