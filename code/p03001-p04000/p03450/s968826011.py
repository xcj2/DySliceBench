N, M = map(int, input().split())


class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        # 根への距離を管理
        self.weight = [0] * n

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            # 親への重みを追加しながら根まで走査
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    # 重さの検索
    def weighting(self, x):
        self.find(x)
        return self.weight[x]

    # 併合
    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        # xの木の高さ < yの木の高さ
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        # xの木の高さ ≧ yの木の高さ
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    # 同じ集合に属するか
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xからyへのコスト
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]


WUF = WeightedUnionFind(N)
for i in range(M):
    l, r, d = map(int, input().split())
    l, r = l-1, r-1
    if WUF.same(l, r):
        if WUF.diff(l, r) != d:
            print("No")
            exit()
    else:
        WUF.union(l, r, d)

print("Yes")
