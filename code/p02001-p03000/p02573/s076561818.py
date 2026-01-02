from sys import stdin
readline = stdin.readline
def r_map(): return map(int, readline().rstrip().split())

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * (n + 1)
        self.rank = [0] * (n + 1)
        self.max_size = 1

    def root(self, x):
        if(self.parents[x] < 0):
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def unite(self, x, y) -> bool:
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.rank[x] > self.rank[y]:
            self.parents[x] += self.parents[y]
            self.parents[y] = x
        else:
            self.parents[y] += self.parents[x]
            self.parents[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
        self.max_size = max(self.max_size, self.size(x))
        return True

    def members(self, x):
        root = self.root(x)
        return [i for i in range(self.n) if self.root(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def is_same(self, x, y) -> bool:
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.parents[self.root(x)]

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}


def main():
    N, M = r_map()
    uf = UnionFind(N)
    for _ in range(M):
        a, b = r_map()
        uf.unite(a, b)
    print(uf.max_size)

if __name__ == "__main__":
    main()
