
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]  # parent. if par[x]==x: x is root.
        self.rank = [0 for i in range(n)]  # depth of tree

    def find(self, x):  # find root
        if(self.par[x] == x):
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if(x == y):
            return

        if(self.rank[x] < self.rank[y]):
            self.par[x] = y
        else:
            self.par[y] = x
            if(self.rank[x] == self.rank[y]):
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def is_root(self, x):
        return self.par[x] == x

    def roots(self):
        return [i for i in range(self.n) if self.is_root(i)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def groups(self):
        return {r: self.members(r) for r in self.roots()}


def main():
    N, M = map(int, input().split())
    p = list(map(int, input().split()))
    p = list(map(lambda x: x - 1, p))

    UF = UnionFind(N)
    for i in range(M):
        x, y = map(int, input().split())
        UF.unite(x - 1, y - 1)

    ans = 0
    for i in range(N):
        if UF.same(i, p[i]):
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
