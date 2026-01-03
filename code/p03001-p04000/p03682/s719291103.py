def d_Built(N, P):
    xs = []
    ys = []
    E = []  # 辺の情報を格納
    for i, (x, y) in enumerate(P):
        xs.append((x, i))
        ys.append((y, i))
    xs.sort()
    ys.sort()

    # 頂点をつなぐ辺の候補を得る
    x_edge = []
    y_edge = []
    for i in range(N - 1):
        # x座標、y座標でソートしたもので隣り合った2点を結ぶ
        x_edge.append((xs[i][1], xs[i + 1][1], xs[i + 1][0] - xs[i][0]))
        y_edge.append((ys[i][1], ys[i + 1][1], ys[i + 1][0] - ys[i][0]))
    x_edge.extend(y_edge)  # 頂点a,頂点b,それを結ぶ辺のコスト
    x_edge.sort(key=lambda x: x[2])  # コストの小さいものから並べる(クラスカル法のため)

    class UnionFind:
        def __init__(self, N):
            self.p = list(range(N))  # 初期状態ではi番の頂点の根(parent)はi番である
            self.rank = [0] * N  # 初期状態ではどの頂点もランクが0とする(何もつながってない)
            self.size = [1] * N  # 初期状態ではどの頂点も連結成分の大きさは1

        def find(self, x):
            # 頂点xが属する連結成分の代表(根の番号)を求める
            if self.p[x] != x:
                # 頂点xの根は他の頂点だった
                self.p[x] = self.find(self.p[x])  # 経路圧縮
            return self.p[x]

        def is_same(self, x, y):
            # 頂点x,yは同じ連結成分に属するか？
            return self.find(x) == self.find(y)

        def union(self, x, y):
            # x,yを同じ連結成分に属させる
            u = self.find(x)
            v = self.find(y)
            if u == v:
                # 同じ連結成分に既に属していた
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

        def get_size(self, x):
            # 頂点xが属する連結成分の大きさ
            return self.size[self.find(x)]

        def show(self):
            return self.p

    uf = UnionFind(N)
    # クラスカル法を使う
    i = 0
    while len(E) != N - 1:
        x1, x2, cost = x_edge[i]
        if uf.find(x1) != uf.find(x2):
            # x1,x2が同じ木に属していた場合、注目している辺を追加するとループを作ってしまう
            uf.union(x1, x2)
            E.append(cost)
        i += 1
    return sum(E)
  
N = int(input())
P = [[int(i) for i in input().split()] for j in range(N)]
print(d_Built(N, P))