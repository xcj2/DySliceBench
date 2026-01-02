# ARC 092 C 最大マッチング問題


class Edge(object):

    def __init__(self, src, dst, cap):
        self.src = src
        self.dst = dst
        self.cap = cap
        self.rev = None

    def create_rev(self):
        """
        対応する残余グラフの辺を作成して返す。
        本来の辺と残余グラフの辺は相互に参照を持ち合うため、このメソッド以外から生成しないこと。
        """
        rev = Edge(self.dst, self.src, 0)
        self.rev = rev
        rev.rev = self
        return rev


class FordFulkerson:

    def __init__(self, N):
        self.N = N
        self.G = [list() for _ in range(N)]  # G[i]: 頂点iに接続している全ての有向辺のリスト

    def add_edge(self, src, dst, cap):
        forward = Edge(src, dst, cap)
        backward = forward.create_rev()
        self.G[src].append(forward)
        self.G[dst].append(backward)

    def flow(self, src, dst):
        max_flow = 0
        while True:
            self.used = [0] * self.N
            flow = self._dfs(src, dst)
            if flow == 0:  # f=0 が返るのは全てのパスを走査してこれ以上検討するパスがなくなったタイミング
                break
            max_flow += flow
        return max_flow

    def _dfs(self, v, t, f=float('inf')):
        """
        深さ優先でグラフを走査し、目的地に達するパスがあるか検索する。
        パスが存在すればその時の最大流を返し、存在しなければ0を返す。
        最大流量がFである時、高々F回のDFSをすることになるため、 O(F|E|) となる。

        :param v: 始点のインデックス
        :param t: 終点のインデックス
        :param f: 現在の再帰スタックにおける暫定の最大流
        """
        if v == t:
            return f
        used = self.used
        used[v] = 1
        for e in self.G[v]:
            if e.cap and not used[e.dst]:
                d = self._dfs(e.dst, t, min(f, e.cap))
                if d:
                    e.cap -= d
                    e.rev.cap += d
                    return d
        return 0


N = int(input())
reds = [tuple(map(int, input().split())) for _ in range(N)]
blues = [tuple(map(int, input().split())) for _ in range(N)]

# 0: s
# 1 to N: reds
# N + 1 to 2N: blues
# 2N + 1: t
ff = FordFulkerson(2 * N + 2)
for i in range(N):
    r_x, r_y = reds[i]
    r_idx = i + 1
    ff.add_edge(0, r_idx, 1)  # sから赤の各点への辺
    for j in range(N):
        b_x, b_y = blues[j]
        b_idx = j + N + 1
        if r_x < b_x and r_y < b_y:
            ff.add_edge(r_idx, b_idx, 1)  # 赤の各点から青の各点への辺
for i in range(N + 1, 2 * N + 1):
    ff.add_edge(i, 2 * N + 1, 1)  # 青の各点からtへの辺

# 最大流 = 最大マッチング数
print(ff.flow(0, 2 * N + 1))