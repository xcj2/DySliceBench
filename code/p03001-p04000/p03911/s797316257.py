# cf16-finalC - Interpretation
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.rank = [0] * (size + 1)

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


def main():
    N, M = map(int, input().split())
    A = [(map(int, input().split())) for _ in range(N)]
    uf, spoken = UnionFind(M), set()
    for _, *langs in A:
        spoken.update(langs)
        primary = langs[0]
        for l in langs[1:]:
            uf.unite(primary, l)
    cur = uf.find(spoken.pop())
    flg = all(uf.find(lang) == cur for lang in spoken)
    print("YES" if flg else "NO")


if __name__ == "__main__":
    main()