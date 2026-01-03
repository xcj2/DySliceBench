# cf16-finalC - Interpretation
class UnionFind:  # O(α(N))
    def __init__(self, size):  # construct a Union-Find tree (1-idx)
        self.parent = [i for i in range(size + 1)]
        self.rank = [0] * (size + 1)

    def find(self, x):  # find the group (root) of a vertex
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):  # unite two groups
        x, y = self.find(x), self.find(y)
        if x == y:  # in the same group
            return
        # unite a small one to a bigger one to balance trees
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


def main():
    # Union-Find on spoken languages -> check all langs are in the same group?
    N, M = map(int, input().split())
    A = tuple(tuple(map(int, input().split())) for _ in range(N))
    uf, spoken = UnionFind(M), set()
    for _, *langs in A:
        spoken.update(langs)
        primary = langs[0]
        for l in langs[1:]:
            uf.unite(primary, l)
    cur = uf.find(spoken.pop())  # group of one of spoken languages
    flg = all(uf.find(lang) == cur for lang in spoken)
    print("YES" if flg else "NO")


if __name__ == "__main__":
    main()