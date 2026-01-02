import sys

input = sys.stdin.readline


class Segtree:
    # https://atcoder.jp/contests/agc038/submissions/7637556
    # の実装を借用しました
    
    # Segment tree
    # 1-indexed
    # 再帰を使わないもの
    # 最小値を求める
    def __init__(self, n, v, func, initial):
        self.initial = initial
        self.func = func
        self.size = 1 << n.bit_length()
        # Segment treeの台の要素数
        self.tree = [self.initial] * (2 * self.size)
        # 1-indexedなので、要素数2*self.size
        # Segment treeの初期値で初期化

        for i in range(n):  # Aを対応する箇所へupdate
            self.tree[i + self.size] = v[i]

        for i in range(self.size - 1, 0, -1):  # 親の部分もupdate
            self.tree[i] = self.func(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, n, x):  # v[n]をxへ更新（反映）
        i = n + self.size
        self.tree[i] = x
        i >>= 1  # 子ノードへ

        while i != 0:
            self.tree[i] = self.func(self.tree[i * 2], self.tree[i * 2 + 1])
            i >>= 1

    def getvalues(self, l, r):  # 区間[l,r)に関するfuncを調べる
        L = l + self.size
        R = r + self.size
        ANS = self.initial

        while L < R:
            if L & 1:
                ANS = self.func(ANS, self.tree[L])
                L += 1

            if R & 1:
                R -= 1
                ANS = self.func(ANS, self.tree[R])
            L >>= 1
            R >>= 1

        return ANS


class UnionFind:
    def __init__(self, n):
        self.v = [-1 for _ in range(n)]

    def find(self, x):
        if self.v[x] < 0:  # (負)は根
            return x
        else:
            self.v[x] = self.find(self.v[x])
            return self.v[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if -self.v[x] < -self.v[y]:
            x, y = y, x
        self.v[x] += self.v[y]
        self.v[y] = x

    def root(self, x):
        return self.v[x] < 0


def main():
    n, k = map(int, input().split())
    p = tuple(int(x) for x in input().split())

    tr1 = Segtree(n, p, min, 1 << 30)
    tr2 = Segtree(n, p, max, -1)

    uf = UnionFind(n)

    cont = 1
    v = None
    for i in range(1, n):
        if p[i - 1] < p[i]:
            cont += 1
        else:
            cont = 1
        if cont >= k:
            # print(i - k + 1)
            if v is None:
                v = i - k + 1
            else:
                uf.unite(v, i - k + 1)
                # print(v, i - k + 1)

    for i in range(n - k):
        # print(f'i:{i} {p[i]} < {tr1.getvalues(i + 1, i + k)} < {tr2.getvalues(i + 1, i + k)} < {p[i + k]}')
        if p[i] < tr1.getvalues(i + 1, i + k) < tr2.getvalues(i + 1, i + k) < p[i + k]:
            uf.unite(i, i + 1)
            # print(i, i + 1)

    ans = sum(uf.root(x) for x in range(n - k + 1))
    print(ans)


if __name__ == '__main__':
    main()
