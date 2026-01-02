class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def root(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.root(x) == self.root(y)


def main():

    V, E = map(int, input().split())

    # need sorted
    edge_q = sorted([tuple(map(int, input().split())) for _ in range(E)], key=lambda x: x[2])

    # kruskal
    ans = 0
    forest = UnionFind(V)
    for s, t, w in edge_q:
        if forest.same(s, t):
            continue
        forest.unite(s, t)
        ans += w
    print(ans)


if __name__ == '__main__':
    main()

