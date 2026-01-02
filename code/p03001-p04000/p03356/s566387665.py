# ARC097D - Equals (ABC097D)
import sys
input = sys.stdin.readline


class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N + 1)]
        self.rank = [0] * (N + 1)

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
        # unite a small one to a bigger one to balance trees
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


def main():
    # check i and Pi are connected components or not
    N, M = tuple(map(int, input().split()))
    P = tuple(map(int, input().split()))
    E = tuple(tuple(map(int, input().split())) for _ in range(M))
    U = UnionFind(N)  # construct a Union-Find tree (1-idx)
    for v, u in E:  # connected components are in the same group
        U.unite(v, u)
    ans = sum(U.is_same(i, p) for i, p in enumerate(P, 1))
    print(ans)


if __name__ == "__main__":
    main()