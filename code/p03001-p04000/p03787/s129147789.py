class UnionFind:
    """素集合を木構造として管理する"""
    def __init__(self, n):
        self.parent = [-1] * n
        self.cnt = n

    def root(self, x):
        """要素xの根を求める"""
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def merge(self, x, y):
        """要素xを含む集合と要素yを含む集合を統合する"""
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        self.cnt -= 1

    def is_same(self, x, y):
        """要素x, yが同じ集合に属するかどうかを求める"""
        return self.root(x) == self.root(y)

    def get_size(self, x):
        """要素xを含む集合の要素数を求める"""
        return -self.parent[self.root(x)]

    def get_cnt(self):
        """集合の個数を求める"""
        return self.cnt


def is_bipartite(graph, s):
    """頂点sを含むgraphが二部グラフかどうかを判定する"""
    n = len(graph)
    stack = [s]
    visited[s] = 0
    is_bi = True
    while stack:
        v = stack.pop()
        for nxt_v in graph[v]:
            if visited[nxt_v] == -1:
                visited[nxt_v] = visited[v] ^ 1
                stack.append(nxt_v)
            elif visited[nxt_v] ^ visited[v] == 0:
                is_bi = False
    return is_bi


n, m = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(m)]


uf = UnionFind(n)
graph = [[] for i in range(n)]
for a, b in edges:
    a -= 1
    b -= 1
    uf.merge(a, b)
    graph[a].append(b)
    graph[b].append(a)


# 連結成分1の要素数
cnt1 = 0
for v in range(n):
    if uf.get_size(v) == 1:
        cnt1 += 1

# 連結成分が1ではない連結成分で二部グラフをなす個数
cnt_bi = 0
# 連結成分が1ではない連結成分で二部グラフをなさない個数
cnt_not_bi = 0

visited = [-1] * n
for v in range(n):
    if visited[v] == -1:
        flag = is_bipartite(graph, v)
        if uf.get_size(v) == 1:
            continue
        if flag:
            cnt_bi += 1
        else:
            cnt_not_bi += 1

ans = n ** 2 - (n - cnt1) ** 2
cnt = cnt_bi + cnt_not_bi
ans += 2 * (cnt_bi ** 2) + (cnt ** 2) - (cnt_bi ** 2)
print(ans)