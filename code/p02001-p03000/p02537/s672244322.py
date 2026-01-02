# Date [ 2020-09-26 21:43:42 ]
# Problem [ d.py ]
# Author Koki_tkg

import sys

def read_str(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline().strip())
def read_ints(): return map(int, sys.stdin.readline().strip().split())
def read_str_split(): return list(sys.stdin.readline().strip())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))

class segtree:
    def __init__(self, op, e, v: list):
        self._n = len(v)
        self.log = ceil_pow2(self._n)
        self.size = 1 << self.log
        self.op = op; self.e = e
        self.d = [self.e()] * (self.size * 2)
        for i in range(self._n): self.d[self.size + i] = v[i]
        for i in range(self.size - 1, 0, -1): self.__update(i)

    def set_(self, p: int, x: int):
        assert 0 <= p and p < self._n
        p += self.size
        self.d[p] = x
        for i in range(1, self.log + 1): self.__update(p >> i)

    def get(self, p: int):
        assert 0 <= p and p < self._n
        return self.d[p + self.size]

    def prod(self, l: int, r: int):
        assert 0 <= l and l <= r and r <= self._n
        l += self.size; r += self.size
        sml, smr = self.e(), self.e()
        while l < r:
            if l & 1: sml = self.op(sml, self.d[l]); l += 1
            if r & 1: r -= 1; smr = self.op(self.d[r], smr)
            l >>= 1; r >>= 1
        return self.op(sml, smr)

    def all_prod(self): return self.d[1]

    def max_right(self, l: int, f):
        assert 0 <= l and l <= self._n
        assert f(self.e())
        if l == self._n: return self._n
        l += self.size
        sm = self.e()
        while True:
            while l % 2 == 0: l >>= 1
            if not f(self.op(sm, self.d[l])):
                while l < self.size:
                    l = 2 * l
                    if f(self.op(sm, self.d[l])):
                        sm = self.op(sm, self.d[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.d[l])
            l += 1
            if (l & -l) == l: break
        return self._n

    def min_left(self, r: int, f):
        assert 0 <= r and r <= self._n
        assert f(self.e())
        if r == 0: return 0
        r += self.size
        sm = self.e()
        while True:
            r -= 1
            while r > 1 and r % 2: r >>= 1
            if not f(self.op(self.d[r], sm)):
                while r < self.size:
                    r = 2 * r + 1
                    if f(self.op(self.d[r], sm)):
                        sm = self.op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.d[r], sm)
            if (r & -r) == r: break
        return 0

    def __update(self, k: int): self.d[k] = self.op(self.d[k * 2], self.d[k * 2 + 1])

def ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n: x += 1
    return x

def op(a, b): return max(a, b)
def e(): return 0

def Main():
    n, k = read_ints()
    A = [read_int() for _ in range(n)]
    seg = segtree(op, e, [0] * 300005)
    seg.set_(A[0], 1)
    for i in range(1, n):
        seg.set_(A[i], seg.prod(max(A[i] - k, 0), min(A[i] + k + 1, 300005)) + 1)
    print(seg.prod(0, 300005))

if __name__ == '__main__':
    Main()
