class DualSegmentTree():

    def __init__(self, n, op, e):
        """
        :param n: 配列の要素数
        :param op: 作用素（モノイド＝結合則＋単位元存在）
        :param e:  単位元
        """
        self.n = n
        self.op = op
        self.e = e
        self.depth = (self.n - 1).bit_length()
        self.size = 1 << self.depth
        self.lazy = [self.e] * ((self.size << 1) + 1)

    def built(self, array):
        """
        arrayを初期値とするセグメント木を構築
        """
        n, size, lazy = self.n, self.size, self.lazy
        for i in range(n):
            lazy[size + i] = array[i]

    def update(self, l, r, x):
        """
        半開区間 [l, r) の各々の要素 a に op(x, a)を作用させる （ 0-indexed ）　（ O(logN) ）
        """
        op, lazy = self.op, self.lazy
        l += self.size
        r += self.size
        self.propagate(l//(l&-l))
        self.propagate((r//(r&-r))-1)
        while l < r:
            if r&1:
                r -= 1              # 半開区間なので先に引いてる
                lazy[r] = op(x, lazy[r])
            if l&1:
                lazy[l] = op(x, lazy[l])
                l += 1
            l >>= 1
            r >>= 1

    def propagate(self, i):
        """
        根から葉に伝搬させる。可換モノイドの場合は更新時の伝搬をサボれる。　（ O(logN) ）
        """
        e, op, lazy = self.e, self.op, self.lazy
        for k in range(i.bit_length()-1, 0,-1):
            x = i>>k
            if lazy[x] == e:
                continue
            lazy[(x<<1)|1] = op(lazy[x], lazy[(x<<1)|1])
            lazy[x<<1] = op(lazy[x], lazy[x<<1])
            lazy[x] = e

    def get(self, i):
        """
        i 番目の値を取得（ 0-indexed ） ( O(logN) )
        """
        i += self.size
        self.propagate(i)
        return self.lazy[i]

    def __getitem__(self, i):
        return self.get(i)

    def __iter__(self):
        n, size, e, op, lazy = self.n, self.size, self.e, self.op, self.lazy
        for x in range(1, size):
            if lazy[x] == e:
                continue
            lazy[(x<<1)|1] = op(lazy[x], lazy[(x<<1)|1])
            lazy[x<<1] = op(lazy[x], lazy[x<<1])
            lazy[x] = e
        for a in lazy[size:size+n]:
            yield a

    def __str__(self):
        n, size, e, op, lazy = self.n, self.size, self.e, self.op, self.lazy
        for x in range(1, size):
            if lazy[x] == e:
                continue
            lazy[(x << 1) | 1] = op(lazy[x], lazy[(x << 1) | 1])
            lazy[x << 1] = op(lazy[x], lazy[x << 1])
            lazy[x] = e
        return str(lazy[size:size + n])

##################################################################################################################
import sys
from bisect import *
input = sys.stdin.readline

N, Q = map(int, input().split())

e = -1
op = lambda x, y: x if x != e else y
st = DualSegmentTree(Q, op, e)

Qu = [list(map(int, input().split())) for _ in range(N)]
Qu.sort(key=lambda x:x[2], reverse=True)

D = [int(input()) for _ in range(Q)]

for q in Qu:
    S, T, X = q
    L = bisect_left(D,S-X)
    R = bisect_left(D,T-X)
    st.update(L, R, X)
print(*st, sep="\n")
