import sys

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.size = [1] * (n+1)  # The number of nodes under the target node.
        self.weight = [0] * (n+1)  # Distance from the root

    def find(self, x):
        if self.root[x] == x:
            return x
        else:
            y = self.find(self.root[x])
            self.weight[x] += self.weight[self.root[x]]
            self.root[x] = y
            return self.root[x]

    def unite(self, x, y, w=0):
        rx = self.find(x)
        ry = self.find(y)
        if self.rank[rx] < self.rank[ry]:
            self.root[rx] = ry
            self.size[ry] += self.size[rx]
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            self.root[ry] = rx
            self.size[rx] += self.size[ry]
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    
    def diff(self, x, y):
        return self.weight[y] - self.weight[x]


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    UF = UnionFind(N)

    for _ in range(M):
        l, r, d = map(int, input().split())
        l -= 1
        r -= 1

        if not UF.is_same(l, r):
            UF.unite(l, r, d)

        elif UF.is_same(l, r) and UF.diff(r, l) != d:
            return 'No'

        else:
            continue

    return 'Yes'


if __name__ == '__main__':
    print(main())
