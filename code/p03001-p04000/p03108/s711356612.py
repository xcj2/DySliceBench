def solve():
    class UnionFind:
        def __init__(self, n):
            self.par = [i for i in range(n)]
            self.rank = [0] * n
            self.size = [1] * n

        # 検索
        def find(self, x):
            if self.par[x] == x:
                return x
            else:
                self.par[x] = self.find(self.par[x])
                return self.par[x]

        # 併合
        def unite(self, x, y):
            x = self.find(x)
            y = self.find(y)

            if x == y:
                return

            if self.rank[x] < self.rank[y]:
                self.par[x] = y
                self.size[y] += self.size[x]
                self.size[x] = 0
            else:
                self.par[y] = x
                self.size[x] += self.size[y]
                self.size[y] = 0
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

        # 同じ集合に属するか判定
        def same(self, x, y):
            return self.find(x) == self.find(y)

        # すべての頂点に対して親を検索する
        def all_find(self):
            for n in range(len(self.par)):
                self.find(n)


    N, M = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(M)]
    uf = UnionFind(N)
    ans = []
    score = N * (N - 1) // 2
    for i in range(M - 1, -1, -1):
        ans.append(score)
        a, b = ab.pop()
        a -= 1
        b -= 1
        pa, pb = uf.find(a), uf.find(b)
        if not uf.same(pa, pb):
            score -= uf.size[pa] * uf.size[pb]
        uf.unite(a, b)
    ans.reverse()
    [print(ans[i]) for i in range(M)]
if __name__ == '__main__' :
    solve()