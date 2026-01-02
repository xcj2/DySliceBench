class Tree():
    def __init__(self, n, decrement=1):
        self.n = n
        self.edges = [[] for _ in range(n)]
        self.edges2 = [[] for _ in range(n)]
        self.root = None
        self.depth = [-1]*n
        self.size = [1]*n       # 部分木のノードの数
        self.color = [[] for _ in range(n)]
        self.cost = [0]*n
        self.decrement = decrement

    def add_edge(self, u, v):
        u, v = u-self.decrement, v-self.decrement
        self.edges[u].append(v)
        self.edges[v].append(u)

    def add_edges(self, edges):
        for u, v, c, d in edges:
            u, v = u-self.decrement, v-self.decrement
            self.edges[u].append(v)
            self.edges[v].append(u)
            self.edges2[u].append((v, c, d))
            self.edges2[v].append((u, c, d))

    def set_root(self, root):
        root -= self.decrement
        self.root = root
        self.par = [-1]*self.n
        self.depth[root] = 0
        self.order = [root]     # 帰りがけに使う
        next_set = [root]
        while next_set:
            p = next_set.pop()
            for q, c, d in self.edges2[p]:
                if self.depth[q] != -1: continue
                self.par[q] = p
                self.color[c].append(q)
                self.cost[q] = d
                self.depth[q] = self.depth[p]+1
                self.order.append(q)
                next_set.append(q)
        for p in self.order[::-1]:
            for q in self.edges[p]:
                if self.par[p] == q: continue
                self.size[p] += self.size[q]

    def heavy_light_decomposition(self):
        """
        heavy edge を並べてリストにした物を返す (1-indexed if decrement=True)
        """
        # assert self.root is not None
        self.vid = [-1]*self.n
        self.hld = [-1]*self.n
        self.head = [-1]*self.n
        self.head[self.root] = self.root
        self.heavy_node = [-1]*self.n
        next_set = [self.root]
        for i in range(self.n):
            """ for tree graph, dfs ends in N times """
            p = next_set.pop()
            self.vid[p] = i
            self.hld[i] = p+self.decrement
            maxs = 0
            for q in self.edges[p]:
                """ encode direction of Heavy edge into heavy_node """
                if self.par[p] == q: continue
                if maxs < self.size[q]:
                    maxs = self.size[q]
                    self.heavy_node[p] = q
            for q in self.edges[p]:
                """ determine "head" of heavy edge """
                if self.par[p] == q or self.heavy_node[p] == q: continue
                self.head[q] = q
                next_set.append(q)
            if self.heavy_node[p] != -1:
                self.head[self.heavy_node[p]] = self.head[p]
                next_set.append(self.heavy_node[p])
        return self.hld

    def lca(self, u, v):
        # assert self.head is not None
        u, v = u-self.decrement, v-self.decrement
        while True:
            if self.vid[u] > self.vid[v]: u, v = v, u
            if self.head[u] != self.head[v]:
                v = self.par[self.head[v]]
            else:
                return u + self.decrement

    def distance(self, u, v):
        # assert self.head is not None
        p = self.lca(u, v)
        u, v, p = u-self.decrement, v-self.decrement, p-self.decrement
        return self.depth[u] + self.depth[v] - 2*self.depth[p]

    def find(self, u, v, x):
        return self.distance(u,x)+self.distance(x,v)==self.distance(u,v)

    def path_to_list(self, u, v, edge_query=False):
        """
        パス上の頂点の集合を self.hld 上の開区間の集合として表す
        ここで、self.hld は heavy edge を並べて数列にしたものである
        """
        # assert self.head is not None
        u, v = u-self.decrement, v-self.decrement
        while True:
            if self.vid[u] > self.vid[v]: u, v = v, u
            if self.head[u] != self.head[v]:
                yield self.vid[self.head[v]], self.vid[v] + 1
                v = self.par[self.head[v]]
            else:
                yield self.vid[u] + edge_query, self.vid[v] + 1
                return

    def point(self, u):
        return self.vid[u-self.decrement]

class SegmentTree:

    def __init__(self, n, op, e):
        """
        :param n: 要素数
        :param op: 二項演算
        :param e: 単位減
        """
        self.n = n
        self.op = op
        self.e = e
        self.size = 1 << (self.n - 1).bit_length()      # st[self.size + i] = array[i]
        self.tree = [self.e] * (self.size << 1)

    def built(self, array):
        """arrayを初期値とするセグメント木を構築"""
        for i in range(self.n):
            self.tree[self.size + i] = array[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.op(self.tree[i<<1], self.tree[(i<<1)|1])

    def update(self, i, x):
        """i 番目の要素を x に更新　(0-indexed) """
        i += self.size
        self.tree[i] = x
        while i > 1:
            i >>= 1
            self.tree[i] = self.op(self.tree[i<<1], self.tree[(i<<1)|1])

    def get(self, l, r):
        """ [l, r)の区間取得の結果を返す　(0-indexed) """
        l += self.size
        r += self.size
        res_l = self.e
        res_r = self.e
        while l < r:
            if l & 1:
                res_l = self.op(res_l, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res_r = self.op(self.tree[r], res_r)
            l >>= 1
            r >>= 1
        return self.op(res_l, res_r)

    def max_right(self, l, f):
        """
        以下の条件を両方満たす r を(いずれか一つ)返す
            ・r = l or f(op(a[l], a[l + 1], ..., a[r - 1])) = true
            ・r = n or f(op(a[l], a[l + 1], ..., a[r])) = false
        """
        if l == self.n: return self.n
        l += self.size
        sm = self.e
        while True:
            while l % 2 == 0: l >>= 1
            if not f(self.op(sm, self.tree[l])):
                while l < self.size:
                    l = 2 * l
                    if f(self.op(sm, self.tree[l])):
                        sm = self.op(sm, self.tree[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.tree[l])
            l += 1
            if (l & -l) == l: break
        return self.n

    def min_left(self, r, f):
        """
        以下の条件を両方満たす l を(いずれか一つ)返す
            ・l = r or f(op(a[l], a[l + 1], ..., a[r - 1])) = true
            ・l = 0 or f(op(a[l - 1], a[l], ..., a[r - 1])) = false
        """
        if r == 0: return 0
        r += self.size
        sm = self.e
        while True:
            r -= 1
            while r > 1 and (r % 2): r >>= 1
            if not f(self.op(self.tree[r], sm)):
                while r < self.size:
                    r = 2 * r + 1
                    if f(self.op(self.tree[r], sm)):
                        sm = self.op(self.tree[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.tree[r], sm)
            if (r & -r) == r: break
        return 0

    def __iter__(self):
        for a in self.tree[self.size:self.size+self.n]:
            yield a

    def __str__(self):
        return str(self.tree[self.size:self.size+self.n])

#########################################################################################################
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
tree = Tree(N)
edges, query = [], [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c, d = map(int, input().split())
    edges.append((a, b, c-1, d))
for i in range(Q):
    c, y, u, v = map(int, input().split())
    query[c-1].append((y, u, v, i))
tree.add_edges(edges)
tree.set_root(1)
hld = tree.heavy_light_decomposition()

e = (0, 0)
op = lambda x, y: (x[0]+y[0], x[1]+y[1])
st = SegmentTree(N, op, e)
res = [0]*Q
for p in range(N):
    st.update(tree.point(p+1), (tree.cost[p],0))
for c in range(N):
    for p in tree.color[c]:
        st.update(tree.point(p+1), (0,1))
    for y, u, v, i in query[c]:
        for l, r in tree.path_to_list(u, v, True):
            cost, cnt = st.get(l, r)
            res[i] += cost + cnt*y
    for p in tree.color[c]:
        st.update(tree.point(p+1), (tree.cost[p],0))

print('\n'.join(map(str,res)))
