def d_equals(N, M, P, S):
    class UnionFind(object):
        def __init__(self, N):
            self.p = list(range(N))  # 初期状態ではi番の頂点の親(parent)はi番
            self.rank = [0] * N  # 初期状態では全頂点がランク0(何もつながってない)
            self.size = [1] * N  # 初期状態ではどの頂点も連結成分の大きさは1

        def find(self, x):  # 頂点xが属する連結成分の代表(根の番号)を求める
            if self.p[x] != x:  # 頂点xの代表は他の頂点だった
                self.p[x] = self.find(self.p[x])  # 経路圧縮(xを代表につなぐ)
            return self.p[x]

        def is_same(self, x, y):  # 頂点x,yは同じ連結成分に属するか？
            return self.find(x) == self.find(y)

        def union(self, x, y):  # x,yを同じ連結成分に属させる
            u = self.find(x)
            v = self.find(y)
            if u == v:  # x,yは既に同じ連結成分に属していた
                return
            if self.rank[u] < self.rank[v]:
                self.p[u] = v  # ランクの大きな方につなげる
                self.size[v] += self.size[u]  # つながっている要素数だけ足す
                self.size[u] = 0  # ランクが小さかった連結成分は「解散」
            else:
                # 上と同様にやる
                self.p[v] = u
                self.size[u] += self.size[v]
                self.size[v] = 0
                if self.rank[u] == self.rank[v]:
                    # 根の分だけ1個「ずれる」
                    self.rank[u] += 1

        def get_size(self, x):  # 頂点xが属する連結成分の大きさ
            return self.size[self.find(x)]

        def show(self):
            return self.p

    ans = 0
    uf = UnionFind(N)
    for a, b in S:
        uf.union(a - 1, b - 1)  # Pのa番とb番は繋がっている(0-indexed)
    for i in range(N):
        if uf.is_same(P[i] - 1, i):
            # 2つが同じ連結成分にあるなら、何回かswapしてp_i=iにできる
            ans += 1
        elif P[i] - 1 == i:
            # 同じ連結成分には属していないが、最初からp_i=iだった
            ans += 1
    return ans

N,M = [int(i) for i in input().split()]
P = [int(i) for i in input().split()]
S = [[int(i) for i in input().split()] for j in range(M)]
print(d_equals(N, M, P, S))