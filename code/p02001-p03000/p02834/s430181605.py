class LCA(object):
    def __init__(self, n, root, edges, decrement=True):
        """
        :param n: 頂点数
        :param root: 木の根
        :param edges: 辺のリスト
        :param decrement:

        :param self.depth: rootを根とした時の各頂点の深さ
        """
        self.n = n
        self.decrement = decrement
        self.root = root - self.decrement
        self.edges = [set() for _ in range(self.n)]
        for x, y in edges:
            self.add_edge(x,y)
        self.k_max = (self.n - 1).bit_length()
        self.depth = [-1 if i != self.root else 0 for i in range(self.n)]
        self.doubling = [[-1] * self.n for _ in range(self.k_max)]
        self.parent = [-1]*self.n
        self.dfs()
        for i in range(1, self.k_max):
            for k in range(self.n):
                if self.doubling[i - 1][k] != -1:
                    self.doubling[i][k] = self.doubling[i - 1][self.doubling[i - 1][k]]

    def add_edge(self, x, y):
        """
        後から追加した場合は update() をする
        """
        if self.decrement:
            x -= 1
            y -= 1
        self.edges[x].add(y)
        self.edges[y].add(x)

    def update(self):
        self.depth = [-1 if i != self.root else 0 for i in range(self.n)]
        self.doubling = [[-1] * self.n for _ in range(self.k_max)]
        self.dfs()
        for i in range(1, self.k_max):
            for k in range(self.n):
                if self.doubling[i - 1][k] != -1:
                    self.doubling[i][k] = self.doubling[i - 1][self.doubling[i - 1][k]]


    def dfs(self):
        next_set = [self.root]
        while next_set:
            p = next_set.pop()
            for q in self.edges[p]:
                if self.depth[q] == -1:
                    self.depth[q] = self.depth[p] + 1
                    self.doubling[0][q] = p
                    next_set += [q]

    def get(self, u, v):
        """
        :return: u と v の最近共通祖先の頂点番号を返す
        """
        if self.decrement:
            u -= 1
            v -= 1
        if self.depth[v] < self.depth[u]:
            u, v = v, u

        for i in range(self.k_max):
            """ v を u の位置まで遡らせる """
            if (self.depth[v] - self.depth[u]) >> i & 1:
                v = self.doubling[i][v]
        if v == u:
            """ v の祖先が u だった場合"""
            return u + self.decrement

        for i in range(self.k_max-1, -1, -1):
            """ k = 2**(k_max-1), ..., 2**0 について、 
            「k個先を確認して共通祖先でないなら u1,v1 をk個先に移動」ということを繰り返す"""
            parent_u, parent_v = self.doubling[i][u], self.doubling[i][v]
            if parent_u != parent_v:
                u, v = parent_u, parent_v
        return self.doubling[0][u] + self.decrement

    def distance(self, u, v):
        """
        :return: u と v の最短距離を求める
        備考: 経路復元をしようとすると O(E)かかるので、経路復元が必要な場合は dfs を用いるとよい
        """
        lca_at = self.get(u,v)
        if self.decrement:
            u -= 1
            v -= 1
            lca_at -= 1
        return self.depth[u] + self.depth[v] - 2*self.depth[lca_at]

    def distance_list(self, start=1, save=False):
        """
        :param start: スタート地点
        :return: スタート地点から各点への距離のリスト
        """
        dist = [-1]*self.n
        if self.decrement:
            start -= 1
        if not save:
            self.parent = [-1] * self.n
        p, t = start, 0
        self.parent[p] = -2
        dist[p] = 0
        next_set = deque([(p, t)])

        while next_set:
            p, t = next_set.popleft()
            for q in self.edges[p]:
                if self.parent[q] != -1:
                    continue
                if q == xx-1:
                    continue
                dist[q] = t + 1
                self.parent[q] = p
                next_set.append((q, t + 1))
        return dist

    def most_distant_point(self, start=1, save=False):
        """
        計算量　O(N)
        :return: (start から最も遠い頂点, 距離)
        """
        if not save:
            self.parent = [-1] * self.n
        res = (start - self.decrement, 0)
        temp = 0
        for i, dist in enumerate(self.distance_list(start, save=save)):
            if dist > temp:
                temp = dist
                res = (i + self.decrement, dist)
        return res

#################################################################################################
import sys
from collections import deque
input = sys.stdin.readline

N, u, v = map(int, input().split())
edges = []
for _ in range(N-1):
    x, y = map(int, input().split())
    edges.append((x,y))
xx = -3
lca = LCA(N, 1, edges, decrement=True)
p = lca.get(u,v)
lu, lv = lca.depth[u-1] - lca.depth[p-1], lca.depth[v-1] - lca.depth[p-1]
if lu <= lv:
    q, _ = lca.most_distant_point(v)
    print(lca.distance(q,v)-1)
    exit()
else:
    L = (lu+lv)//2
    cnt = 0
    lca.distance_list()
    if lca.depth[u-1] >= lca.depth[v-1]:
        a = u-1
        while cnt < L:
            a = lca.parent[a]
            cnt += 1
        xx, s = lca.parent[a]+1, a+1
    else:
        a = v-1
        while cnt < L+1:
            a = lca.parent[a]
            cnt += 1
        xx, s = a+1, lca.parent[a]+1
    q, _ = lca.most_distant_point(s)
    print(lca.distance(q,v)-1)
    exit()