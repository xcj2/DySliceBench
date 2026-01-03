# https://atcoder.jp/contests/abc065/tasks/arc076_b

from heapq import heappush, heappop

class UnionFind(object):
    def __init__(self, n):
        self.n = n
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

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]

    def group_count(self):
        return len(self.roots())

N = int(input())
X, Y = [], []
Loc = []
for n in range(N):
    xi, yi = map(int, input().split())
    X.append((xi, n))
    Y.append((yi, n))
    Loc.append((n, xi, yi))

# LocX = sorted(Loc, key=lambda x: x[1])
# LocY = sorted(Loc, key=lambda x: x[2])

# edges = set({})
# for i in range(1, N - 1):
#     es = [(LocX[i-1][0], LocX[i][0]), \
#           (LocX[i+1][0], LocX[i][0]), \
#           (LocY[i-1][0], LocY[i][0]), \
#           (LocY[i+1][0], LocY[i][0])]
#     for ii, jj in es:
#         if ii < jj:
#             edges.add((ii, jj))

# print(N)
# print(edges)
# pedges = [(min(abs(X[i] - X[j]), abs(Y[i] - Y[j])), i, j) for (i, j) in edges] 
# pedges.sort()
# print(pedges)

# uf = UnionFind(N)
# total = 0
# for (cost, i, j) in pedges:
#     if uf.unite(i, j):
#         total += cost
# print(total)


# Xでソートして隣接，Yでソートして隣接を辺とみなす
edges = []
X.sort()
Y.sort()
for i in range(N - 1):
    wxi = abs(X[i][0] - X[i + 1][0])
    wyi = abs(Y[i][0] - Y[i + 1][0])
    heappush(edges, (wxi, X[i][1], X[i + 1][1]))
    heappush(edges, (wyi, Y[i][1], Y[i + 1][1]))

# Kruskal
uf = UnionFind(N)
cost = 0
while len(edges) > 0:
    (w, u, v) = heappop(edges)
    if uf.unite(u, v):
        cost += w
print(cost)