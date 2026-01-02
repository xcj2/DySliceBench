class UnionFind():
    def __init__(self, n):
        self.parent = [-1 for _ in range(n)]
        # 正==子: 根の頂点番号 / 負==根: 連結頂点数

    def find(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        else:
            if self.size(x) < self.size(y):
                x, y = y, x
            self.parent[x] += self.parent[y]
            self.parent[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        x = self.find(x)
        return -self.parent[x]


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())

    g = tuple(reversed(tuple((int(x) - 1 for x in input().split()) for _ in range(m))))
    t = n * (n - 1) // 2

    ret = [t]  # 最後反転
    uf = UnionFind(n)
    for a, b in g[:-1]:
        if not uf.same(a, b):
            t -= uf.size(a) * uf.size(b)
        ret.append(t)
        uf.unite(a, b)
    ret.reverse()
    print(*ret, sep='\n')


if __name__ == '__main__':
    main()
