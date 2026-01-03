def d_Connectivity(N, K, L, R, T):  # 都市数、道路数、鉄道数、都市の道路/鉄道による結び
    class UnionFind:
        def __init__(self, N):
            self.p = list(range(N))  # 初期状態ではi番の頂点の根(parent)はi番である
            self.rank = [0] * N  # 初期状態ではどの頂点もランクが0とする(何もつながっていない)
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

    road = UnionFind(N)  # 道路による町のつながり
    train = UnionFind(N)  # 鉄道による町のつながり
    for p, q in R:
        road.union(p - 1, q - 1)
    for r, s in T:
        train.union(r - 1, s - 1)

    from collections import defaultdict
    d = defaultdict(int)
    for i in range(N):
        d[road.find(i), train.find(i)] += 1  # 道路も鉄道もつながっている
    ans = (d[road.find(i), train.find(i)] for i in range(N))
    return ' '.join(str(i) for i in ans)

N,K,L = [int(i) for i in input().split()]
R = [[int(i) for i in input().split()] for j in range(K)]
T = [[int(i) for i in input().split()] for j in range(L)]
print(d_Connectivity(N, K, L, R, T))