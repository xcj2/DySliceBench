class UnionFind():
    def __init__(self, n):
        self.n = n  # 要素の総数．
        self.parents = [-1] * n  # 各要素の親要素の番号を格納するリスト．要素がrootの場合は-(そのグループの要素数)を返す

    def find(self, x):
        """要素xが属するグループの根を返す"""
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """要素xが属するグループと要素yが属するグループとを併合する"""
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """要素xが属するグループの要素数を返す"""
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """要素x, yが同じグループに属するかどうかを返す"""
        return self.find(x) == self.find(y)

    def members(self, x):
        """要素xが属するグループに属する要素をリストで返す"""
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """全ての根の要素をリストで返す"""
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """グループの数を返す"""
        return len(self.roots())

    def all_group_members(self):
        """{ルート要素: [そのグループの要素のリスト]} の辞書を返す"""
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def main():
    N, M, K = map(int, input().split())
    cnt = [0] * N
    uf = UnionFind(N)

    for _ in range(M):
        A, B = map(lambda x: int(x)-1, input().split())
        cnt[A] += 1
        cnt[B] += 1
        uf.union(A, B)

    for _ in range(K):
        C, D = map(lambda x: int(x)-1, input().split())
        if uf.same(C, D):
            cnt[C] += 1
            cnt[D] += 1

    for i in range(N):
        print(uf.size(i) - cnt[i] - 1, end=" ")


if __name__ == '__main__':
    main()

