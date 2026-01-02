class WeightedUnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        # 親ノードとの重み
        self.diff_weight = [0 for i in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        # 親ノードはまだ上書きしない
        root = self.find(self.par[x])
        self.diff_weight[x] += self.diff_weight[self.par[x]]
        self.par[x] = root
        return self.par[x]

    def weight(self, x):
        # xの根に対する重みを返す
        self.find(x)
        return self.diff_weight[x]

    def diff(self, x, y):
        #xの根と yの根の差分をとる
        return self.weight(y) - self.weight(x)

    def unite(self, x, y, w):
        # ノード x の下にノード y をつける。辺の重みは w
        # x の根と y の 根をくっつけるのでwを補正する
        w += self.weight(x)
        w -= self.weight(y)
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            # y の下に x をつけることになるので、重さは反転させる
            self.par[x] = y
            w = -w
            self.diff_weight[x] = w
        elif self.rank[y] < self.rank[x]:
            self.par[y] = x
            self.diff_weight[y] = w
        else:
            self.par[y] = x
            self.rank[x] += 1
            self.diff_weight[y] = w

n, m = map(int, input().split())
wuf = WeightedUnionFind(n)
for i in range(m):
    l, r, d = map(int, input().split())
    l -= 1
    r -= 1
    if wuf.find(l) == wuf.find(r):
        if wuf.diff(l, r) != d:
            print('No')
            exit()
    else:
        wuf.unite(l, r, d)
else:
    print('Yes')