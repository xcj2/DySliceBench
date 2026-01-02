from collections import Counter


class UnionFind:
    def __init__(self, node_size):
        self.node_size = node_size
        self.parent = [i for i in range(self.node_size)]    # parent's number
        self.rank = [0 for i in range(self.node_size)]
        self.size = [1 for i in range(self.node_size)]

    # find root of x
    def root(self, x):
        if self.parent[x] == x:    # x is a root
            return x
        else:
            self.parent[x] = self.root(self.parent[x])    # path compression
            return self.parent[x]

    # judge whether x is connected to y. returns boolian.
    def is_connected(self, x, y):
        return self.root(x) == self.root(y)

    # connects x to y
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
            else:
                self.parent[y] = x
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1
            self.size[x] += self.size[y]
            self.size[y] = self.size[x]

    def get_size(self, x):
        x = self.root(x)
        return self.size[x]


def main():
    N, M = map(int, input().split())    # N islands, M bridges
    bridge_list_a = [0 for i in range(M)]
    bridge_list_b = [0 for i in range(M)]
    for i in range(M):
        bridge_list_a[i], bridge_list_b[i] = map(int, input().split())
    bridge_list_a.reverse()
    bridge_list_a = [a - 1 for a in bridge_list_a]
    bridge_list_b.reverse()
    bridge_list_b = [b - 1 for b in bridge_list_b]

    Islands = UnionFind(N)

    inconvenience = N * (N - 1) // 2
    ans = [inconvenience]

    for ai, bi in zip(bridge_list_a, bridge_list_b):
        if not Islands.is_connected(ai, bi):
            inconvenience -= Islands.get_size(ai) * Islands.get_size(bi)

        ans.append(inconvenience)
        Islands.unite(ai, bi)

    ans.reverse()
    for inconvenience in ans[1:]:
        print(inconvenience)


if __name__ == "__main__":
    main()
