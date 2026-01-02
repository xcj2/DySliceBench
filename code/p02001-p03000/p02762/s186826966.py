from collections import defaultdict


class UnionFind:
    def __init__(self, N):
        self.N = N  # ノード数
        # 親ノードを示す。負は自身が親ということ。親だった場合は−(その集合のサイズ)
        self.parent = [-1] * N

    def root(self, A):
        # Aがどのグループに属しているか調べる
        # ノード番号を受けとって一番上の親ノードの番号を返す
        # print(A)
        if self.parent[A] < 0:
            return A
        self.parent[A] = self.root(self.parent[A])
        return self.parent[A]

    def size(self, A):
        # 自分のいるグループの頂点数を調べる
        return -self.parent[self.root(A)]

    def unite(self, A, B):
        # AとBをくっつける
        # AとBを直接つなぐのではなく、root(A)にroot(B)をくっつける
        A = self.root(A)
        B = self.root(B)

        if A == B:
            return False  # すでにくっついてるからくっつけない

        if self.size(A) < self.size(B):
            # 大きい方(A)に小さいほう(B)をくっ付けたい
            # 大小が逆だったらひっくり返しちゃう。
            A, B = B, A

        # Aのサイズを更新する
        self.parent[A] += self.parent[B]
        # Bの親をAに変更する
        self.parent[B] = A

        return True

    def same(self, A, B):
        return self.root(A) == self.root(B)


N, M, K = map(int, input().split())


uf = UnionFind(N)
# frd = [0] * N  # 友達の数

frd = defaultdict(int)

blk = [[] for _ in range(N)]  # ブロック関係。隣接リスト
ans = [0] * N

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    frd[a] += 1
    frd[b] += 1
    uf.unite(a, b)
for i in range(K):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    blk[a].append(b)
    blk[b].append(a)
for i in range(N):
    ans[i] = uf.size(i) - 1 - frd[i]
    for j in blk[i]:
        if uf.same(i, j):
            ans[i] -= 1  # 同じグループ内でのblock関係を引く
print(*ans)

