class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def root(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return

        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self, x, y):
        return self.root(x) == self.root(y)


def main():
    n, m = map(int, input().split())
    ps = list(map(int, input().split()))

    # 1-origin
    union_find = UnionFind(n + 1)
    for i in range(m):
        x, y = map(int, input().split())
        union_find.unite(x, y)

    ans = 0
    for key, value in enumerate(ps, 1):
        if union_find.same(key, value):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
