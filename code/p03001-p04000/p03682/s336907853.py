def d_built(N, P):
    class UnionFind(object):
        def __init__(self, n):
            self.p = list(range(n))  # i番の頂点の親(parent)はi番とする
            self.rank = [0] * n  # 全頂点はランク0(繋がりなし)とする
            self.size = [1] * n  # 全頂点の連結成分の大きさ1とする

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
            # 経路圧縮を行い、連結成分の代表を更新
            self.find(x)
            self.find(y)
            return None

        def find(self, x):  # 頂点xが属する連結成分の代表(根の番号)を求める
            if self.p[x] != x:  # 頂点xの代表は他の頂点だった
                self.p[x] = self.find(self.p[x])  # 経路圧縮(xを代表につなぐ)
            return self.p[x]

        def is_same(self, x, y):  # 頂点x,yは同じ連結成分に属するか？
            return self.find(x) == self.find(y)

    xs, ys = [], []
    for i, (x, y) in enumerate(P):
        xs.append((x, i))
        ys.append((y, i))
    xs.sort()
    ys.sort()

    # 頂点をつなぐ辺の候補を得る
    x_edge, y_edge = [], []
    for i in range(N - 1):
        # x座標、y座標でソートしたもので隣り合った2点を結ぶ
        x_edge.append((xs[i][1], xs[i + 1][1], xs[i + 1][0] - xs[i][0]))
        y_edge.append((ys[i][1], ys[i + 1][1], ys[i + 1][0] - ys[i][0]))
    x_edge.extend(y_edge)  # 頂点a-b間を結ぶ辺のコスト
    x_edge.sort(key=lambda x: x[2])  # コストの小さいものから並べる(クラスカル法のため)

    # クラスカル法による
    uf = UnionFind(N)
    edges = []  # 辺の情報を格納
    for x1, x2, cost in x_edge:
        if not uf.is_same(x1, x2):
            # x1, x2が同じ木に属していた場合、注目した辺を加えると閉路ができる
            uf.union(x1, x2)
            edges.append(cost)
        if len(edges) == N - 1:
            break
    return sum(edges)

N = int(input())
P = [[int(i) for i in input().split()] for j in range(N)]
print(d_built(N, P))