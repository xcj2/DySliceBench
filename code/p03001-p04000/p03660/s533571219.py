from collections import defaultdict

class Tree:
    def __init__(self, n, edges, weight=False):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.parent = [-1] * self.n
        self.children = [[] for _ in range(self.n)]
        self.dist = [-1] * self.n  # 根からの距離
        self.depth = [-1] * self.n  # 根からの深さ(cost=1での距離)
        self.weight = defaultdict(lambda: 10**18)
        if weight:
            for u, v, weight in edges:
                self.adj[u].append(v)
                self.adj[v].append(u)
                self.weight[(u, v)] = weight
                self.weight[(v, u)] = weight
        else:
            for u, v in edges:
                self.adj[u].append(v)
                self.adj[v].append(u)
                self.weight[(u, v)] = 1
                self.weight[(v, u)] = 1

    def set_root(self, root):  # O(n)
        self.root = root
        self.order = [root]
        self.dist[root] = 0
        self.depth[root] = 0
        stack = [root]
        while stack:
            v = stack.pop()
            for child in self.adj[v]:
                if child == self.parent[v]:
                    continue
                else:
                    self.parent[child] = v
                    self.children[v].append(child)
                    self.dist[child] = self.dist[v] + self.weight[(v, child)]
                    self.depth[child] = self.depth[v] + 1
                    self.order.append(child)
                    stack.append(child)

    def get_root_path(self, target):
        path = [target]
        v = target
        while v != self.root:
            path.append(self.parent[v])
            v = self.parent[v]
        path.reverse()
        return path

    def get_diameter(self, restore=False):  # double-sweepで求める  O(n)
        u = self.dist.index(max(self.dist))  # 根から一番遠いものを根とし、そこから一番遠いものを見つける
        dist_u = [-1] * self.n
        dist_u[u] = 0
        stack = [u]
        parent_u = [None for _ in range(self.n)]
        while stack:
            v = stack.pop()
            for child in self.adj[v]:
                if dist_u[child] == -1:
                    dist_u[child] = dist_u[v] + self.weight[(v, child)]
                    parent_u[child] = v
                    stack.append(child)
        diameter = max(dist_u)
        v = dist_u.index(diameter)
        if restore:
            path = [v]
            while v != u:
                v = parent_u[v]
                path.append(v)
            path.reverse()  # [u,...,v]
            return diameter, path
        else:
            return diameter, u, v

    # --- Heavy Light Decomposition --- #

    def heavy_light_decompose(self):  # O(n)
        self.subsize = [1] * self.n  # 部分木の要素数(自分含む)
        self.head = [self.root] * self.n  # 分割された各部分木の先頭
        self.tree_order = [0] * self.n

        # 末端の方から各頂点の部分木の要素数(subsize)を計算していって、
        # heavy-nodeがchildren[v][0]に来るようにする
        for v in reversed(self.order):
            v_kids = self.children[v]  # 名前が長いのでalias
            for i, child in enumerate(v_kids):
                self.subsize[v] += self.subsize[child]
                if self.subsize[child] > self.subsize[v_kids[0]]:
                    v_kids[i], v_kids[0] = v_kids[0], v_kids[i]

        # それぞれのnodeについて分割されたchianの先頭(head)を記録
        # また、DFSの行きがけ順をtree_orderとする headの浅い順でchainが入る
        stack = [self.root]
        tree_label = 0
        while stack:
            v = stack.pop()
            self.tree_order[v] = tree_label
            tree_label += 1
            for child in reversed(self.children[v]):  # スタックを使ったdfsのため逆にしておく
                if child == self.children[v][0]:
                    self.head[child] = self.head[v]
                else:
                    self.head[child] = child  # light-nodeは切り離されたsub-treeのheadになる
                stack.append(child)

    def get_hld_chain_paths(self, u, v):  # (u,v)間の経路をchainごとに返す [l,r)
        ret = []
        while True:
            if self.tree_order[u] > self.tree_order[v]:
                u, v = v, u
            if self.head[u] == self.head[v]:
                ret.append((self.tree_order[u], self.tree_order[v] + 1))
                return ret
            else:
                ret.append((self.tree_order[self.head[v]], self.tree_order[v] + 1))
                v = self.parent[self.head[v]]

    def get_hld_lca(self, u, v):  # Lowest Common Ancestor
        while True:  # head[u] = head[v] になるまで遡る
            if self.tree_order[u] > self.tree_order[v]:
                u, v = v, u
            if self.head[u] == self.head[v]:
                return u
            v = self.parent[self.head[v]]

    def get_hld_distance(self, u, v):
        return self.dist[u] + self.dist[v] - (2 * self.dist[self.get_hld_lca(u, v)])

    def exist_on_path_hld(self, u, v, x):  # u,v間の最短経路上にxがあるかどうか
        return self.get_hld_distance(u, x) + self.get_hld_distance(x, v) == self.get_hld_distance(u, v)

# ---------------------- #

n = int(input())
edges = [tuple(int(x) - 1 for x in input().split()) for _ in range(n - 1)]
tree = Tree(n, edges)
tree.set_root(0)
tree.heavy_light_decompose()
dist = tree.get_hld_distance(0, n - 1)
snuke = n - 1
for _ in range((dist - 1) // 2):
    snuke = tree.parent[snuke]
snuke_size = tree.subsize[snuke]
fennec_size = n - snuke_size
if snuke_size >= fennec_size:
    print("Snuke")
else:
    print("Fennec")
