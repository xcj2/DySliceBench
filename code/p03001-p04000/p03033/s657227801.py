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
                self.lazy[r] = self.op(x, self.lazy[r])
            if l&1 == 0:
                self.lazy[l] = self.op(x, self.lazy[l])
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
            self.lazy[2*x+1] = self.op(self.lazy[x], self.lazy[2*x+1])
            self.lazy[2*x+2] = self.op(self.lazy[x], self.lazy[2*x+2])
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
            self.lazy[2*x+1] = self.op(self.lazy[x], self.lazy[2*x+1])
            self.lazy[2*x+2] = self.op(self.lazy[x], self.lazy[2*x+2])
            self.lazy[x] = self.e
        for a in self.lazy[self.size-1:self.size-1+self.n]:
            yield a

    def __str__(self):
        for x in range(self.size-1):
            if self.lazy[x] == self.e:
                continue
            self.lazy[2*x+1] = self.op(self.lazy[x], self.lazy[2*x+1])
            self.lazy[2*x+2] = self.op(self.lazy[x], self.lazy[2*x+2])
            self.lazy[x] = self.e
        return str(self.lazy[self.size-1:self.size-1 + self.n])

class ListList:
    """ tupleを一番目の添え字に関してソートする"""
    def __init__(self, max_value_list):
        """
        :param max_value_list: tuple = (i, j, k) を考えた時、  max_value_list = (j_max, k_max)
        """
        self.list_list = []
        self.separation = [0]
        self.max_value_list = list(map(lambda x: x.bit_length(), max_value_list))
        for a in self.max_value_list:
            self.separation.append(self.separation[-1] + a)
        self.separation.reverse()
        self.mask = list(map(lambda x: x-1, self.separation))

    def append(self, array):
        temp = 0
        for x, i in zip(array, self.separation):
            temp += x<<i
        self.list_list.append(temp)

    def sort(self, reverse=False):
        return self.list_list.sort(reverse=reverse)

    def __getitem__(self, item):
        temp = self.list_list[item]
        array = []
        for a in self.max_value_list:
            array = [temp&((1<<a)-1)] + array
            temp>>=a
        array = [temp] + array
        return array

    def __iter__(self):
        for i in range(len(self.list_list)):
            yield self[i]

    def __str__(self):
        text = []
        for a in self:
            text.append("[" + ", ".join(list(map(str, a))) + "]")
        return "[" + ", ".join(text) + "]"

##################################################################################################################
import sys
from bisect import *
input = sys.stdin.readline

N, Q = map(int, input().split())

e = -1
op = lambda x, y: x if x != e else y
st = DualSegmentTree(Q, op, e)

Qu = ListList([10**9,10**9])
for _ in range(N):
    S, T, X = map(int, input().split())
    Qu.append((X, S, T))
Qu.sort(reverse=True)

D = [int(input()) for _ in range(Q)]

for q in Qu:
    X, S, T = q
    L = bisect_left(D,S-X)
    R = bisect_left(D,T-X)
    st.update(L, R, X)
print(*st, sep="\n")