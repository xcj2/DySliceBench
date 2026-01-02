
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
    E = [[int(x) - 1 for x in input().split()] for _ in range(M)]

    ans = 0
    for i in range(M):
        uf = UnionFind(N)
        # i番目の辺を除くすべての辺をつないぐ
        for j, e in enumerate(E):
            if i == j:
                continue
            uf.union(e[0], e[1])
        # i番目の辺を除くすべての辺をつないだあとで、i番目の辺(a, b)がつながるかを判定する
        # つながらないならば、そのi番目の辺は橋である
        a, b = E[i]
        if not uf.is_same(a, b):
            ans += 1
    print(ans)

if __name__ == "__main__":
    resolve()