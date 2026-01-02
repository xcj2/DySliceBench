def d_decayed_bridges(N, M, Bridges):
    class UnionFind(object):
        def __init__(self, n):
            self.p = list(range(n))  # i番の頂点の親(parent)をi番で初期化
            self.rank = [0] * n  # 全頂点はランク0(何もつながってない)
            self.size = [1] * n  # どの頂点も連結成分の大きさ1

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

        def find(self, x):  # 頂点xが属する連結成分の代表(根の番号)を求める
            if self.p[x] != x:  # 頂点xの代表は他の頂点だった
                self.p[x] = self.find(self.p[x])  # 経路圧縮(xを代表につなぐ)
            return self.p[x]

        def is_same(self, x, y):  # 頂点x,yは同じ連結成分に属するか？
            return self.find(x) == self.find(y)

        def get_size(self, x):  # 頂点xが属する連結成分の大きさ
            return self.size[self.find(x)]

    uf = UnionFind(N + 1)
    ans_tmp = [N * (N - 1) // 2]
    for a, b in reversed(Bridges):
        if uf.is_same(a, b):
            ans_tmp.append(ans_tmp[-1])
        else:
            ans_tmp.append(ans_tmp[-1] - (uf.get_size(a) * uf.get_size(b)))
        uf.union(a, b)
    ans_tmp.pop()
    ans = '\n'.join(map(str, ans_tmp[::-1]))
    return ans

N, M = [int(i) for i in input().split()]
Bridges = [[int(i) for i in input().split()] for j in range(M)]
print(d_decayed_bridges(N, M, Bridges))