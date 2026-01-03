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

    def size(self, x):
        return -self.parents[self.root(x)]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def members(self, x):
        root = self.root(x)
        return [i for i in range(self.n) if self.root(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    
    N = int(input())
    
    x, y = [[0, 0] for _ in range(N)], [[0, 0] for _ in range(N)]
    for i in range(N):
        x[i][0], y[i][0] = map(int, input().split())
        x[i][1], y[i][1] = i, i
    x, y = sorted(x), sorted(y)
    
    L = [[0, 0, 0] for _ in range((N - 1) * 2)]
    for i in range(N - 1):
        L[i * 2][0] = x[i + 1][0] - x[i][0]
        L[i * 2][1] = x[i][1]
        L[i * 2][2] = x[i + 1][1]
        L[i * 2 + 1][0] = y[i + 1][0] - y[i][0]
        L[i * 2 + 1][1] = y[i][1]
        L[i * 2 + 1][2] = y[i + 1][1]
    L = sorted(L)

    tree = UnionFind(N)
    ans = 0
    for i in range((N - 1) * 2):
        if not tree.same(L[i][1], L[i][2]):
            ans += L[i][0]
            tree.unite(L[i][1], L[i][2])
    print(ans)
    

if __name__ == '__main__':
    main()
