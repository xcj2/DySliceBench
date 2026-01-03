import sys
from collections import Counter
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same_check(self, x, y):
        return self.find(x) == self.find(y)


n, k, l = map(int, input().split())
road = UnionFind(n)
for i in range(k):
    p, q = map(int, input().split())
    road.union(p, q)

rail = UnionFind(n)
for i in range(l):
    r, s = map(int, input().split())
    rail.union(r, s)

r = [(road.find(i + 1), rail.find(i + 1)) for i in range(n)]
c = Counter(r)
ans = []
for i in range(n):
    ans.append(c[r[i]])
print(' '.join(map(str, ans)))
