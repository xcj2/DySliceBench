from collections import defaultdict


class UnionFind():
    # nはノードの数
    def __init__(self, n):
        self.n = n
        self.parents = [-1]*n  # 根のノードは限らないので注意

    # xはノードの番号
    def find(self, x):  # あるノードの親を探すためのメソッド
        if self.parents[x] < 0:  # 親の場合、そのグラフの要素の個数を負の値で保持している
            return x
        else:
            # 再帰的に親を探しにいき、得られた値を格納する
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # x, yはノードの番号
    def union(self, x, y):
        x = self.find(x)  # 根の番号を取得
        y = self.find(y)  # 根の番号を取得
        if x == y:
            return  # 同じ親ならば合体させる必要はない

        # ※ それぞれ要素の個数が負の値で格納されている
        if self.parents[x] > self.parents[y]:
            # yのグループの方が要素の個数が多い場合 (yの方が値が小さいということは、負の世界では値が大きいため)
            # 必ずxの方が要素が多い状態にする
            x, y = y, x

        self.parents[x] += self.parents[y]  # 負の値同士だが、これで良い
        self.parents[y] = x  # yは親ではなくなったため、新しい親であるxの値を正でもつ

    # xはノードの番号
    def size(self, x):
        # 親まで辿ればグループの大きさが負の値で格納されているため、それにマイナスをつけてreturnする
        return -self.parents[self.find(x)]

    # x, yはノードの番号
    def same(self, x, y):
        # 親が同じ = 同じグループに属するならTrueがreturnされる
        return self.find(x) == self.find(y)

    # xはノードの番号
    def members(self, x):
        root = self.find(x)  # 親の値を取得する
        # findで再帰的に親の値が獲得できる
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        # 親となっているノードの番号をリストでreturnする
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_counts(self):
        # グループの数をreturnする
        return len(self.roots())

    def all_group_members(self):
        # 親のノードの番号をキーにして、子のノードの番号を対応させた辞書を返す
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        # printした時の表記
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


H, W = map(int, input().split())
gridgraph = [input() for _ in range(H)]

# 定義するときはUnionFind(要素数)
uf = UnionFind(H*W)
# 木を定義する
for i in range(H):
    for j in range(W):
        if 0 <= i < H-1:  # 最終行でないのであれば実行
            if gridgraph[i][j] != gridgraph[i+1][j]:
                uf.union(W*i+j, W*(i+1)+j)  # 要素の番号の振り方はこうやる

        if 0 <= j < W-1:  # 最終列でないのであれば実行
            if gridgraph[i][j] != gridgraph[i][j+1]:
                uf.union(W*i+j, W*i+j+1)  # 要素の番号の振り方はこうやる

# 根の番号をキーにして、その連結成分に黒, 白それぞれいくつ入っているかを管理する辞書
black = defaultdict(int)
white = defaultdict(int)
for i in range(H):
    for j in range(W):
        if gridgraph[i][j] == "#":
            black[uf.find(W*i+j)] += 1
        else:
            white[uf.find(W*i+j)] += 1
ans = 0
for u in uf.roots():
    ans += black[u] * white[u]
print(ans)
