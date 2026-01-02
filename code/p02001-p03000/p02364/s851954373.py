# solve 64 by Kruskal algorithm

class UnionFind(object):
    def __init__(self, n):
        self.par = [-1] * n
    
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return False
        else:
            if self.par[x] > self.par[y]:
                x, y = y, x
            self.par[x] += self.par[y]
            self.par[y] = x
            return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.par[self.find(x)]


# グラフの読み込み
from heapq import heappush, heappop
edges = []
N, M = map(int, input().split())
for _ in range(M):
    si, ti, wi = map(int, input().split())
    heappush(edges, (wi, si, ti))

# クラスカル法
uf = UnionFind(N)
cost = 0
mst = []
while len(edges) > 0:
    (w, u, v) = heappop(edges)
    if not uf.same(u, v):
        uf.unite(u, v)
        mst.append((u, v))
        cost += w

print(cost)
# print(mst)
