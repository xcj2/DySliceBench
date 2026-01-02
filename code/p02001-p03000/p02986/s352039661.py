import bisect
from collections import deque


class LowestCommonAncestor():
    """根付き木に対して、二頂点の共通の祖先で最も近いところにある頂点を求める
    初期化(ダブリング配列parent[k][v]の構築): O(NlogN)
    lcaを求めるクエリ: O(logN)
    """
    def __init__(self, tree, root):
        self.n = len(tree)
        self.depth = [0] * self.n
        self.log_size = (self.n).bit_length()
        self.parent = [[-1] * self.n for i in range(self.log_size)]

        # 親を2^0回たどって到達する頂点、つまり現在の頂点に対する親の頂点を求める
        # parent[0][現在の頂点] = 親の頂点
        q = deque([(root, -1, 0)]) # (現在の地点, 親の頂点, 現在の頂点と親の頂点間の距離) 
        while q:
            v, par, dist = q.pop()
            self.parent[0][v] = par
            self.depth[v] = dist
            for child_v, _, _ in tree[v]:
                if child_v != par:
                    self.depth[child_v] = dist + 1
                    q.append((child_v, v, dist + 1))

        # ダブリングで親を2^k回たどって到達する頂点を求める
        for k in range(1, self.log_size):
            for v in range(self.n):
                self.parent[k][v] = self.parent[k-1][self.parent[k-1][v]]
            
    def lca(self, u, v):
        # u, vのうち深いところにある方から|depth[u] - depth[v]|だけ親をたどる
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        for k in range(self.log_size):
            if (self.depth[v] - self.depth[u] >> k) & 1:
                v = self.parent[k][v]
        if u == v:
            return u
          
        # 二分探索でLCAを求める
        for k in reversed(range(self.log_size)):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][u]
 

def euler_tour(tree: list, root: int):
    """根をrootとしたときの辺に対するオイラーツアーを行う
    posの部分木が区間[begin[pos], end[pos])に対応する
    """
    n = len(tree)
    trail = []
    weight = []
    color = []
    begin = [-1] * n
    end = [-1] * n
    par = {root: -1}
    stack = [(root, 0, 0)]

    while stack:
        v, c, col = stack.pop()
        if v >= 0:  # 行きがけ順の処理
            trail.append(v)
            weight.append(c)
            color.append(col)
            begin[v] = len(trail) - 1
            end[v] = len(trail)
            stack.append((~v, -c, col))
            for nxt_v, nxt_c, nxt_col in tree[v]:
                if nxt_v not in par:
                    par[nxt_v] = v
                    stack.append((nxt_v, nxt_c, nxt_col))

        else:  # 帰りがけ順の処理
            if ~v == root:
                continue
            trail.append(par[~v])
            weight.append(c)
            color.append(col)
            end[par[~v]] = len(trail)

    return trail, weight, color, begin, end


n, q = map(int, input().split())
info = [list(map(int, input().split())) for i in range(n - 1)]
query = [list(map(int, input().split())) for i in range(q)]

tree = [[] for i in range(n)]
for a, b, col, dist in info:
    a -= 1
    b -= 1
    tree[a].append((b, dist, col))
    tree[b].append((a, dist, col))

trail, weight, color, begin, end = euler_tour(tree, 0)

# 辺の重みを色ごとに累積和する
w_col = [[0] for i in range(n)]
for i in range(len(weight)):
    col = color[i]
    w_col[col].append(weight[i] + w_col[col][-1])

# 辺の個数を色ごとに累積和する
cnt_col = [[0] for i in range(n)]
for i in range(len(weight)):
    col = color[i]
    cnt_col[col].append(int(2 * (weight[i] >= 1)) - 1 + cnt_col[col][-1])

# 色ごとのインデックス
ind = [[] for i in range(n)]
for i in range(len(weight)):
    col = color[i]
    ind[col].append(i)

# 辺の重みを累積和にする
for i in range(len(weight) - 1):
    weight[i + 1] += weight[i]

lca = LowestCommonAncestor(tree, 0)
for x, y, u, v in query:
    u -= 1
    v -= 1
    lca_uv = lca.lca(u, v)

    ans = weight[begin[u]] + weight[begin[v]] - 2 * weight[begin[lca_uv]]

    l = bisect.bisect_right(ind[x], begin[u])
    r = bisect.bisect_right(ind[x], begin[v])
    mid = bisect.bisect_right(ind[x], begin[lca_uv])
    
    cnt = cnt_col[x][r] + cnt_col[x][l] - 2 * cnt_col[x][mid]
    w = w_col[x][r] + w_col[x][l] - 2 * w_col[x][mid]
    
    print(abs(ans) + abs(cnt) * y - abs(w))