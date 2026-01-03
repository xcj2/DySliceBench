from operator import itemgetter

class UnionFind:  # 0-index
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n  # 親の番号 要素が根の場合は-(そのグループの要素数)を格納

    def find(self, x):  # 要素xが属するグループの根を返す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):  # 要素xが属するグループと要素yが属するグループとを併合する
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):  # 要素xが属するグループのサイズ（要素数）を返す
        return -self.parents[self.find(x)]

    def same(self, x, y):  # 要素x, yが同じグループに属するかどうかを返す
        return self.find(x) == self.find(y)

    def members(self, x):  # 要素xが属するグループに属する要素をリストで返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):  # すべての根の要素をリストで返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):  # グループの数を返す
        return len(self.roots())

    def all_group_members(self):  # {根: [グループに含まれる要素のリスト], ...}の辞書を返す
        return {root: self.members(root) for root in self.roots()}

# ---------------------- #

def kruskal(n, edges):  # edges := [(u, v, weight), ...] weightでソート済み O(E)
    uf = UnionFind(n)
    ret = 0
    for u, v, w in edges:
        if not uf.same(u, v):
            ret += w
            uf.union(u, v)
    return ret

# ---------------------- #

n = int(input())
XY = []
for i in range(n):
    x, y = (int(x) for x in input().split())
    XY.append((i, x, y))

edges = []
XY.sort(key=itemgetter(1))
for (u, x1, _), (v, x2, _) in zip(XY, XY[1:]):
    edges.append((u, v, abs(x2 - x1)))

XY.sort(key=itemgetter(2))
for (u, _, y1), (v, _, y2) in zip(XY, XY[1:]):
    edges.append((u, v, abs(y2 - y1)))

edges.sort(key=itemgetter(2))
ans = kruskal(n, edges)
print(ans)
