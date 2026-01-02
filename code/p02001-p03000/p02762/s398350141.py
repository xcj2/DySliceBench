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


N, M, K = map(int, input().split())
uf = UnionFind(N)
friends = defaultdict(int)
for _ in range(M):  # 友達関係の数
    a, b = map(lambda x: int(x)-1, input().split())
    uf.union(a, b)
    friends[a] += 1
    friends[b] += 1
blocked = defaultdict(list)
for _ in range(K):  # ブロック関係の人数
    c, d = map(lambda x: int(x)-1, input().split())
    blocked[c].append(d)
    blocked[d].append(c)
ans = []
for i in range(N):
    # 同じグループの人数
    group_size = uf.size(i)
    # iと直接友達の人数
    i_frends = friends[i]
    # ブロック関係の人の中で、同じグループの人を数える
    cnt = 0
    for b in blocked[i]:
        if uf.same(i, b):
            cnt += 1
    ans.append(group_size - i_frends - cnt - 1)
print(" ".join(map(str, ans)))
