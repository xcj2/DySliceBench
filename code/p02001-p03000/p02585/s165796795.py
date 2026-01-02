def solve():
    from collections import defaultdict
    class UnionFind():
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
                return

            if self.par[x] > self.par[y]:
                x, y = y, x

            self.par[x] += self.par[y]
            self.par[y] = x

        def size(self, x):
            return -self.par[self.find(x)]

        def same(self, x, y):
            return self.find(x) == self.find(y)

    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    mp = defaultdict(int)
    uf = UnionFind(n)

    for i in range(n):
        uf.unite(i, p[i] - 1)

    for i in range(n):
        mp[uf.find(i)] += c[i]# 根にループ一周のポイントを加算

    ans = -10 ** 14
    for i in range(n):
        roop = uf.size(i) # ループに関連する要素数
        times = (k - 1) // roop if mp[uf.find(i)] > 0 else 0# 一周後のポイントが正ならループ回数をストック
        over = max(min(roop, k - roop * times), 1)# 最終周の移動数
        tmp = 0
        s = -10 ** 10
        idx = i
        for j in range(over):# 最終周のポイント最大値
            tmp += c[idx]
            s = max(s, tmp)
            idx = p[idx] - 1
        s += times * mp[uf.find(i)]# 最終週までの累積ポイント加算
        ans = max(ans, s)
    print(ans)


solve()
