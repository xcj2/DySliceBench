import sys

sys.setrecursionlimit(10 ** 9)


class UnionFind:
    def __init__(self, n):
        self.v = [-1 for _ in range(n)]  # 根(負): 連結頂点数 * (-1) / 子(正): 根の頂点番号(0-indexed)

    def find(self, x):  # xを含む木における根の頂点番号を返す
        if self.v[x] < 0:  # (負)は根
            return x
        else:  # 根の頂点番号
            self.v[x] = self.find(self.v[x])  # uniteでは, 旧根に属する頂点の根が旧根のままなので更新
            return self.v[x]

    def unite(self, x, y):  # 違う根に属していたらrankが低くなるように連結
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if -self.v[x] < -self.v[y]:  # size比較, 　(-1) * (連結頂点数 * (-1)), (正)同士の大小比較
            x, y = y, x  # 連結頂点数が少ない方をyにすると, findでの更新回数が減る？
        self.v[x] += self.v[y]  # 連結頂点数の和を取る, 連結頂点数 * (-1)
        self.v[y] = x  # 連結頂点数が少ないy(引数yの根の頂点番号)の根をx(引数xの根の頂点番号)にする

    def root(self, x):
        return self.v[x] < 0  # (負)は根

    def same(self, x, y):
        return self.find(x) == self.find(y)  # 同じ根に属するか

    def size(self, x):
        return -self.v[self.find(x)]  # 連結頂点数を返す


N = int(input())
e = [[] for _ in range(N)]
uf = UnionFind(N)
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    # 0-indexedに直した
    e[u].append((v, w))
    e[v].append((u, w))

    uf.same(u, v)

# e[点]:=(隣接頂点,長さ)

root = uf.find(0)
# 根

ans = [None] * N
ans[root] = 0

# print(e)


def rec(vv):
    for nv, w in e[vv]:
        if ans[nv] is not None: continue
        ans[nv] = (ans[vv] + w) % 2
        rec(nv)


rec(root)

print(*ans, sep='\n')
