# Union-Find木（サイズ付き）
class UnionFind():
    # 初めは全ての頂点が別々の木の根
    def __init__(self, n):  # n要素で初期化
        self.parent = [None] * n # 親
        self.rank = [None] * n   # 木の深さ
        self._size = [1] * n # 要素が属する集合の大きさ（根の要素のみ参照すること）
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def root_of(self, x):
        children = [x]
        while self.parent[x] != x:
            # px = self.parent[x]
            x = self.parent[x]
            children.append(x)

        for ch in children:
            self.parent[ch] = x

        return x

    # xとyの属する集合を併合
    def union(self, x, y):
        rx = self.root_of(x)
        ry = self.root_of(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]: # ランクの小さい木から大きい木の根に辺を張る
            self.parent[rx] = ry  # rxをryの子とする
            self._size[ry] += self._size[rx]
        else:
            self.parent[ry] = rx
            self._size[rx] += self._size[ry]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    # 同じ集合に属するかどうか
    def same(self, x, y):
        return self.root_of(x) == self.root_of(y)


def kruskal(E, n):
    '''
    E ... (辺のコスト, (始点, 終点))のリスト
    n ... 頂点の数
    '''
    E.sort()
    cost = 0
    uf = UnionFind(n)
    for c, (x, y) in E:
        if not uf.same(x, y):
            cost += c
            uf.union(x, y)
    return cost

n, m = [int(x) for x in input().split()]
E = []
for _ in range(m):
    s, t, w = [int(x) for x in input().split()]
    E.append((w, (s, t)))

print(kruskal(E, n))

