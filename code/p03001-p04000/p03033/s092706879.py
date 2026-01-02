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
        for i in range(self.n):
            self.lazy[self.size + i] = array[i]

    def update(self, l, r, x):
        """
        半開区間 [l, r) の各々の要素 a に op(x, a)を作用させる （ 0-indexed ）　（ O(logN) ）
        """
        l += self.size
        r += self.size
        l0 = l//(l&-l)
        r0 = r//(r&-r)
        self.propagate(l0)
        self.propagate(r0-1)
        while l < r:
            if r&1:
                r -= 1              # 半開区間なので先に引いてる
                self.lazy[r] = self.op(x, self.lazy[r])
            if l&1:
                self.lazy[l] = self.op(x, self.lazy[l])
                l += 1
            l >>= 1
            r >>= 1

    def propagate(self, i):
        """
        根から葉に伝搬させる。可換モノイドの場合は更新時の伝搬をサボれる。　（ O(logN) ）
        """
        for k in range(self.depth, 0,-1):
            x = i>>k
            if self.lazy[x] == self.e:
                continue
            self.lazy[(x<<1)|1] = self.op(self.lazy[x], self.lazy[(x<<1)|1])
            self.lazy[x<<1] = self.op(self.lazy[x], self.lazy[x<<1])
            self.lazy[x] = self.e

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
        for x in range(1, self.size):
            if self.lazy[x] == self.e:
                continue
            self.lazy[(x<<1)|1] = self.op(self.lazy[x], self.lazy[(x<<1)|1])
            self.lazy[x<<1] = self.op(self.lazy[x], self.lazy[x<<1])
            self.lazy[x] = self.e
        for a in self.lazy[self.size:self.size+self.n]:
            yield a

    def __str__(self):
        for x in range(1, self.size):
            if self.lazy[x] == self.e:
                continue
            self.lazy[(x<<1)|1] = self.op(self.lazy[x], self.lazy[(x<<1)|1])
            self.lazy[x<<1] = self.op(self.lazy[x], self.lazy[x<<1])
            self.lazy[x] = self.e
        return str(self.lazy[self.size:self.size + self.n])

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