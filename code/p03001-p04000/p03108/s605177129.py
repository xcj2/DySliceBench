
class UnionFind():
    # 各要素の親要素の番号を格納するリスト
    # 要素が根（ルート）の場合は-(そのグループの要素数)を格納する
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # 要素xが属するグループの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # 要素xが属するグループと要素yが属するグループとを併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # 要素xが属するグループのサイズ（要素数）を返す
    def size(self, x):
        return -self.parents[self.find(x)]

    # 要素x, yが同じグループに属するかどうかを返す
    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    # 要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    # すべての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    # グループの数を返す
    def group_count(self):
        return len(self.roots())

    # {ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    # ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す (print()での表示用)
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def resolve():
    N, M = map(int, input().split())
    G = [list(map(lambda x:int(x)-1, input().split())) for _ in range(M)]

    # なくなる橋は、1番目の辺を削除、2番目の辺を削除なので1・2の辺がない状態
    # 3番目の辺を削除なので1・2・3番目の辺がない状態・・・と変化していく
    # よって、単純に後ろの辺から追加していく
    uf = UnionFind(N)
    pair = N * (N - 1) // 2 # aからbの島の組み合わせ
    ans = []
    for a, b in G[::-1]:
        ans.append(pair)
        # 連結しているか判定
        if not uf.is_same(a, b):
            n_a = uf.size(a)
            n_b = uf.size(b)
            pair -= n_a * n_b

        # 時間を巻き戻し(追加していく)
        uf.union(a, b)

    print("\n".join(map(str, ans[::-1])))

if __name__ == "__main__":
    resolve()