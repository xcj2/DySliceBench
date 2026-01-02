import sys
s2nn = lambda s: [int(c) for c in s.split(' ')]
ss2nn = lambda ss: [int(s) for s in ss]
ss2nnn = lambda ss: [s2nn(s) for s in ss]
i2s = lambda: sys.stdin.readline().rstrip()
i2n = lambda: int(i2s())
i2nn = lambda: s2nn(i2s())
ii2ss = lambda n: [sys.stdin.readline().rstrip() for _ in range(n)]
ii2sss = lambda n: [list(sys.stdin.readline().rstrip()) for _ in range(n)]
ii2nn = lambda n: ss2nn(ii2ss(n))
ii2nnn = lambda n: ss2nnn(ii2ss(n))

class UnionFind:
    # n: 要素数
    def __init__(self, n):
        # par[i] < 0 ならば根（初期状態では全て根）
        # 根の場合、(集合サイズ * -1) を表す
        self.parents = [-1 for i in range(n)]

    # 要素iの根を求める
    def root(self, i):
        pi = self.parents[i]
        if pi < 0:
            return i
        else:
            ri = self.root(pi)
            self.parents[i] = ri
            return ri

    # 同じ集合か否か
    def issame(self, i, j):
        return self.root(i) == self.root(j)

    # 集合を併合
    def merge(self, i, j):
        ri = self.root(i)
        rj = self.root(j)
        if ri == rj:
            return
        if ri > rj:
            ri, rj = rj, ri
        self.parents[ri] += self.parents[rj]
        self.parents[rj] = ri

    # 属する集合サイズ
    def size(self, i):
        return -self.parents[self.root(i)]

def main():
    N, M = i2nn()
    AB = ii2nnn(M)
    n = N * (N-1) // 2  # 不便さの初期値
    nn = [n] * (M)
    uf = UnionFind(N)
    for i in range(len(AB)-1, 0, -1):
        a, b = AB[i]
        a -= 1
        b -= 1
        if uf.root(a) != uf.root(b):
            n -= uf.size(a) * uf.size(b)
            uf.merge(a, b)
        nn[i-1] = n

    for n in nn:
        print(n)

main()
