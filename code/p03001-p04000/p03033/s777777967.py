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
        self.size = 1 << (self.n - 1).bit_length()
        self.lazy = [self.e] * (self.size << 1)

    def update(self, l, r, x):
        """
        半開区間 [l, r) の値を x に更新 （ 0-indexed ）　（ O(logN) ）
        """
        l += (self.size - 1)
        r += (self.size - 1)
        self.propagate(l)
        self.propagate(r-1)
        while l < r:
            if r&1 == 0:
                r -= 1              # 半開区間なので先に引いてる
                self.lazy[r] = x
            if l&1 == 0:
                self.lazy[l] = x
                l += 1
            l = (l - 1) // 2
            r = (r - 1) // 2

    def propagate(self, i):
        """
        根から葉に伝搬させる。可換モノイドの場合は更新時の伝搬をサボれる。　（ O(logN) ）
        """
        tmp = []
        while i>0:
            i -= 1
            i >>= 1
            tmp.append(i)
        for x in reversed(tmp):
            if self.lazy[x] == self.e:
                continue
            self.lazy[2*x+1] = self.lazy[x]
            self.lazy[2*x+2] = self.lazy[x]
            self.lazy[x] = self.e

    def get(self, i):
        """
        i 番目の値を取得（ 0-indexed ） ( O(logN) )
        """
        i += (self.size - 1)
        self.propagate(i)
        return self.lazy[i]

    def __getitem__(self, i):
        return self.get(i)

    def __iter__(self):
        for x in range(self.size-1):
            if self.lazy[x] == self.e:
                continue
            self.lazy[2*x+1] = self.lazy[x]
            self.lazy[2*x+2] = self.lazy[x]
            self.lazy[x] = self.e
        for a in self.lazy[self.size-1:self.size-1+self.n]:
            yield a

    def __str__(self):
        for x in range(self.size-1):
            if self.lazy[x] == self.e:
                continue
            self.lazy[2*x+1] = self.lazy[x]
            self.lazy[2*x+2] = self.lazy[x]
            self.lazy[x] = self.e
        return str(self.lazy[self.size-1:self.size-1 + self.n])

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