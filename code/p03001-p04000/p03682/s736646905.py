from heapq import heappop, heappush


class UnionFind(object):

    def __init__(self, N):
        self.tree = [i for i in range(N)]
        self.rank = [0] * (N + 1)
        self.size = [1] * N  # 頂点iの属する連結成分の大きさ

    def find(self, x):
        while self.tree[x] != self.tree[self.tree[x]]:
            self.tree[x] = self.tree[self.tree[x]]  # 経路圧縮
        return self.tree[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        # ランクを考慮しない場合はどちらが親になっても良い
        if self.rank[x] < self.rank[y]:
            self.tree[x] = y
            self.size[y] += self.size[x]
        else:
            self.tree[y] = x
            self.size[x] += self.size[y]

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def has_same_parent(self, x, y):
        return self.find(x) == self.find(y)


def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))


N = I()
X = [None] * N
Y = [None] * N
for i in range(N):
    x, y = MI()
    X[i] = (x, i, x, y)
    Y[i] = (y, i, x, y)
X.sort()
Y.sort()

# ある頂点vから最小全域木に含まれる点をたどった先の頂点は、x軸方向で最も近いかy軸方向で最もvから近いはず
q = list()
for i in range(N - 1):
    for axis in [X, Y]:
        _, t0, x0, y0 = axis[i]
        _, t1, x1, y1 = axis[i + 1]
        cost = min(abs(x1 - x0), abs(y1 - y0))
        heappush(q, (cost, t0, t1))

# Kruskal法 := 最小コストの辺から順に見て、新たな頂点が仲間に入るなら加える
uf = UnionFind(N)
ans = 0
while len(q) > 0:
    cost, t0, t1 = heappop(q)
    if not uf.has_same_parent(t0, t1):
        uf.unite(t0, t1)
        ans += cost
print(ans)
