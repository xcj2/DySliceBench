class UnionFind():
    def __init__(self, n):
        self.parent = [-1 for _ in range(n)]
        # 正==子: 根の頂点番号 / 負==根: 連結頂点数

    def find(self, x):
        #要素xが属するグループの根を返す
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        #要素xが属するグループと要素yが属するグループとを併合する
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        else:
            if self.size(x) < self.size(y):
                x, y = y, x
            self.parent[x] += self.parent[y]
            self.parent[y] = x

    def same(self, x, y):
        #要素x, yが同じグループに属するかどうかを返す
        return self.find(x) == self.find(y)

    def size(self, x):
        #要素xが属するグループのサイズ（要素数）を返す
        x = self.find(x)
        return -self.parent[x]

    def is_root(self, x):
        #すべての根の要素をリストで返す
        return self.parent[x] < 0

    def members(self, x):
        #要素xが属するグループに属する要素をリストで返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def group_count(self):
        #グループの数を返す
        return len(self.roots())

    def all_group_members(self):
        #{ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す
        return {r: self.members(r) for r in self.roots()}
#############################################################
import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')
ans = int(0)

N, M = LI()
AB = [LI() for _ in range(M)]

dp = [0]*M
dp[M-1] = N*(N - 1)//2

uf = UnionFind(N)

for i in range(M-1, 0, -1):
    x = AB[i][0] - 1
    y = AB[i][1] - 1
    if uf.same(x, y):
        #x,yが同じ木にある時
        dp[i-1] = tmp
    else:
        xs = uf.size(x)
        ys = uf.size(y)
        uf.unite(x, y)
        tmp = dp[i] - xs * ys
        dp[i-1] = tmp
        if tmp==0:
            break
#    print(uf.find(x),uf.find(y))
for i in range(M):
    print(dp[i])

