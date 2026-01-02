import sys


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.root[x] == x:
            return x
        else:
            y = self.find(self.root[x])
            self.root[x] = y
            return self.root[x]

    def unite(self, x, y):
        if self.is_same(x, y):
            return
        rx = self.find(x)
        ry = self.find(y)
        if self.rank[rx] < self.rank[ry]:
            self.root[rx] = ry
        else:
            self.root[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    uft = UnionFind(N)
    for _ in range(M):
        x, y, _ = map(int, input().split())
        uft.unite(x, y)

    root = set()
    for i in range(1, N+1):
        root.add(uft.find(i))

    return len(root)


if __name__ == '__main__':
    print(main())
