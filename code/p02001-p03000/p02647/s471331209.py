import sys
input = sys.stdin.readline
import math


class RAQ():
    
    def __init__(self, size):
        """初期化"""
        self.size = size
        n = 2 ** ((size-1).bit_length())
        treesize = n * 2
        st = [0] * treesize
        self.st = st
        self.offset = len(st) // 2

    @classmethod
    def from_array(cls, a):
        st = cls(len(a))
        for i, x in enumerate(a):
            st.add(i, i+1, x)
        return st

    def _add_topdown(self, a, b, value, k=1, l=0, r=-1):
        """区間[a, b) に対する加算
        k: 着目しているノード (1-indexed)
        l: 探索区間 st[l, r) の左端 (0-indexed)
        r: 探索区間 st[l, r) の右端 (0-indexed)
        """
        if r == -1:
            r = self.offset
        if r <= a or b <= l:
            return
        if l == r - 1:
            self.st[k] += value
            return
        if a <= l and r <= b:
            self.st[k] += value
            return
        mid = (l + r) // 2
        self._add(a, b, value, k * 2, l, mid)
        self._add(a, b, value, k * 2 + 1, mid, r)

    def _add_bottomup(self, a, b, value):
        """区間[a, b) に対する加算
        """
        a += self.offset
        b += self.offset - 1
        while a < b:
            if a & 1:
                self.st[a] += value
                a += 1
            a >>= 1
            if not b & 1:
                self.st[b] += value
                b -= 1
            b >>= 1
        if a == b:
            self.st[a] += value

    def add(self, a, b, value):
        """区間[a, b) に対する加算"""
        if a > b:
            raise ValueError("a must be less than equal b.")
        return self._add_bottomup(a, b, value)

    def get(self, key):
        """値の取得"""
        offset = len(self.st) // 2
        k = offset + key
        v = self.st[k]
        k >>= 1
        while k > 0:
            v += self.st[k]
            k >>= 1
        return v


def read():
    N, K = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    return N, K, A


def solve(N, K, A):
    KL = N.bit_length() * 2 + 4
    if K > KL:
        print(*([N] * N))
        return
    raq = RAQ.from_array(A)
    a = [0 for i in range(N)]

    for k in range(min(K, KL)):
        for i in range(N):
            a[i] = raq.get(i)
            raq.add(i, i+1, -a[i])
        for i in range(N):
            l = max(0, i-a[i])
            r = min(N, i+1+a[i])
            raq.add(l, r, 1)
    print(*[raq.get(i) for i in range(N)])


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
