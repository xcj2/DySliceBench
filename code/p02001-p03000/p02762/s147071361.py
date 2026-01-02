def d_friend_suggestions():
    N, M, K = [int(i) for i in input().split()]
    Friends = [[int(i) - 1 for i in input().split()] for j in range(M)]
    Blocked = [[int(i) - 1 for i in input().split()] for j in range(K)]

    class UnionFind(object):
        def __init__(self, n):
            """要素番号は 0 スタートを前提とする"""
            self.num_element = n
            self.parents = [-1] * n  # 要素が根の場合は、-(グループの要素数) を格納

        def find(self, x):
            """要素 x が属するグループの根を返す"""
            if self.parents[x] < 0:
                return x
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

        def union(self, x, y):
            """要素 x が属するグループと要素 y が属するグループとを併合する"""
            u, v = self.find(x), self.find(y)

            if u == v:
                return

            # u のグループの方が要素数が少なかった (parents の 定義より)
            if self.parents[u] > self.parents[v]:
                u, v = v, u

            self.parents[u] += self.parents[v]  # u と同グループの要素数を増やす
            self.parents[v] = u  # v は u に繋げる

        def get_size(self, x):
            """要素 x が属するグループの要素数を返す"""
            return -self.parents[self.find(x)]

        def is_same(self, x, y):
            """要素 x, y は同じグループに属するか？"""
            return self.find(x) == self.find(y)

    uf = UnionFind(N)
    degree = [0] * N
    for a, b in Friends:
        uf.union(a, b)
        degree[a] += 1
        degree[b] += 1
    for c, d in Blocked:
        if uf.is_same(c, d):
            degree[c] += 1
            degree[d] += 1

    ans = [uf.get_size(i) - 1 - degree[i] for i in range(N)]
    return ' '.join(map(str, ans))

print(d_friend_suggestions())