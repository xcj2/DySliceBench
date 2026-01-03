class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            x, y = y, x
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        self.size[x] += self.size[y]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]
      
from collections import Counter


def abc049_d():
    n, k, l = map(int, input().split())

    road = UnionFind(n)
    for i in range(k):
        p, q = map(int, input().split())
        road.unite(p - 1, q - 1)

    rail = UnionFind(n)
    for i in range(l):
        r, s = map(int, input().split())
        rail.unite(r - 1, s - 1)

    set1 = []
    for i in range(n):
        set1.append((road.find(i), rail.find(i)))
    c = Counter(set1)
    ans = []
    for i in range(n):
        ans.append(c[(road.find(i), rail.find(i))])
    print(*ans)


if __name__ == '__main__':
    abc049_d()
