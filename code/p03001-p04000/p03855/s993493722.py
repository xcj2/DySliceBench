import sys
from collections import defaultdict

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
    N, K, L = map(int, input().split())
    road = UnionFind(N)
    rail = UnionFind(N)

    for _ in range(K):
        p, q = map(int, input().split())
        road.unite(p-1, q-1)

    for _ in range(L):
        r, s = map(int, input().split())
        rail.unite(r-1, s-1)

    d = defaultdict(lambda: 0)
    for i in range(N):
        n = road.find(i)
        m = rail.find(i)
        d[(n, m)] += 1

    ans = []
    for i in range(N):
        n = road.find(i)
        m = rail.find(i)
        ans.append(d[(n, m)])

    return print(*ans)


if __name__ == '__main__':
    main()
