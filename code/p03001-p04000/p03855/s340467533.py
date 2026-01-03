from collections import Counter


class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]

    def root(self, i):
        if self.parents[i] == i:
            return i
        else:
            self.parents[i] = self.root(self.parents[i])
            return self.parents[i]

    def unite(self, i, j):
        self.parents[self.root(self.parents[i])] = self.root(j)

    def is_unite(self, i, j):
        return self.root(i) == self.root(j)


def solve(N, K, L, PQs, RSs):
    road_cities = UnionFind(N)
    train_cities = UnionFind(N)

    for p, q in PQs:
        road_cities.unite(p, q)
    for r, s in RSs:
        train_cities.unite(r, s)

    counts = Counter([
        (road_cities.root(i), train_cities.root(i))
        for i in range(1, N + 1)
    ])

    ans = [
        counts[(road_cities.root(i), train_cities.root(i))]
        for i in range(1, N + 1)
    ]

    return " ".join([str(c) for c in ans])


if __name__ == "__main__":
    N, K, L = map(int, input().split(" "))
    PQs = []
    RSs = []
    for _ in range(K):
        PQs.append(tuple(map(int, input().split(" "))))
    for _ in range(L):
        RSs.append(tuple(map(int, input().split(" "))))
    print(solve(N, K, L, PQs, RSs))
