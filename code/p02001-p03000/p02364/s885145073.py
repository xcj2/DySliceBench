# GRL_2_A - Minimum Spanning Tree
class UnionFind:  # O(α(N))
    def __init__(self, size):  # construct a Union-Find tree (1-idx)
        self.parent = [i for i in range(size)]
        self.rank = [0] * (size)
        self.size = size

    def find(self, x):  # find the group (root) of a vertex
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def is_same(self, x, y):  # check two vertices are in the same group
        return self.find(x) == self.find(y)

    def unite(self, x, y):  # unite two groups
        x, y = self.find(x), self.find(y)
        if x == y:  # the same group
            return
        # unite a smaller one to a bigger one in order to balance trees
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


def kruskal() -> int:
    total_cost, undetermined, uf = 0, N, UnionFind(N)
    for cost, v, u in E:
        if not uf.is_same(v, u):
            uf.unite(v, u)
            total_cost += cost
            undetermined -= 1
        if not undetermined:
            break
    return total_cost


def main():
    global N, E
    N, M, *E = map(int, open(0).read().split())
    E = [(c, v, u) for (v, u, c) in zip(*[iter(E)] * 3)]
    E.sort()
    ans = kruskal()
    print(ans)


if __name__ == "__main__":
    main()
