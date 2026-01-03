
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
##############################

class UnionFind:
    def __init__(self, N):
        self.rank = [0] * N
        self.parent = [i for i in range(N)]
        self.n = N

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if (x == y):
            return

        if (self.rank[x] < self.rank[y]):
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

# https://atcoder.jp/contests/abc049/submissions/3095247

from collections import Counter

N,K,L = map(int,input().split())
roads = [tuple(map(lambda x:int(x)-1,input().split())) for i in range(K)]
rails = [tuple(map(lambda x:int(x)-1,input().split())) for i in range(L)]

uf_road = UnionFind(N)
for a,b in roads:
    uf_road.unite(a,b)

uf_rail = UnionFind(N)
for a,b in rails:
    uf_rail.unite(a,b)

ctr = Counter()
for i in range(N):
    r1 = uf_road.find(i)
    r2 = uf_rail.find(i)
    ctr[(r1,r2)] += 1

ans = []
for i in range(N):
    r1 = uf_road.find(i)
    r2 = uf_rail.find(i)
    ans.append(ctr[(r1,r2)])

print(*ans)
