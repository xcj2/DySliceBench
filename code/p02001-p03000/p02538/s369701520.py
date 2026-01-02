# Date [ 2020-09-26 22:17:31 ]
# Problem [ e.py ]
# Author Koki_tkg

#from __future__ import annotations
import sys

def read_str(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline().strip())
def read_ints(): return map(int, sys.stdin.readline().strip().split())
def read_str_split(): return list(sys.stdin.readline().strip())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))

class lazy_segtree:
    def __init__(self, op, e, mapping, composition, id, v: list):
        self.op = op; self.e = e; self.mapping = mapping; self.composition = composition; self.id = id
        self._n = len(v)
        self.log = ceil_pow2(self._n)
        self.size = 1 << self.log
        self.lz = [self.id()] * self.size
        self.d = [self.e()] * (2 * self.size)
        for i in range(self._n): self.d[self.size + i] = v[i]
        for i in range(self.size - 1, 0, -1): self.__update(i)

    def set_(self, p: int, x: int):
        assert 0 <= p and p < self._n
        p += self.size
        for i in range(self.log, 0, -1): self.__push(p >> i)
        self.d[p] = x
        for i in range(1, self.log + 1): self.__update(p >> 1)

    def get(self, p: int):
        assert 0 <= p and p < self._n
        p += self.size
        for i in range(self.log, 0, -1): self.__push(p >> i)
        return self.d[p]

    def prod(self, l: int, r: int):
        assert 0 <= l and l <= r and r <= self._n
        if l == r: return self.e()
        l += self.size; r += self.size

        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l: self.__push(l >> i)
            if ((r >> i) << i) != r: self.__push(r >> i)

        sml, smr = self.e(), self.e()
        while l < r:
            if l & 1: sml = self.op(sml, self.d[l]); l += 1
            if r & 1: r -= 1; smr = self.op(self.d[r], smr)
            l >>= 1; r >>= 1

        return self.op(sml, smr)

    def all_prod(self): return self.d[1]

    def apply_sub(self, p: int, f):
        assert 0 <= p and p < self._n
        p += self.size
        for i in range(self.log, 0, -1): self.__push(p >> i)
        self.d[p] = self.mapping(f, self.d[p])
        for i in range(1, self.log + 1): self.__update(p >> 1)

    def apply(self, l: int, r: int, f):
        assert 0 <= l and l <= r and r <= self._n
        if l == r: return
        l += self.size; r += self.size

        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l: self.__push(l >> i)
            if ((r >> i) << i) != r: self.__push((r - 1) >> i)

        l2, r2 = l, r
        while l < r:
            if l & 1: self.__all_apply(l, f); l += 1
            if r & 1: r -= 1; self.__all_apply(r, f)
            l >>= 1; r >>= 1
        l, r = l2, r2

        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l: self.__update(l >> i)
            if ((r >> i) << i) != r: self.__update(r >> i)

    def max_right(self, l: int, g):
        assert 0 <= l and l <= self._n
        if l == self._n: return self._n
        l += self.size
        for i in range(self.log, 0, -1): self.__push(l >> i)
        sm = self.e()
        while True:
            while l % 2 == 0: l >>= 1
            if not g(self.op(sm, self.d[l])):
                while l < self.size:
                    self.__push(l)
                    l = 2 * l
                    if g(self.op(sm, self.d[l])):
                        sm = self.op(sm, self.d[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.d[l])
            l += 1
            if (l & -l) == l: break
        return self._n

    def min_left(self, r: int, g):
        assert 0 <= r and r <= self._n
        if r == 0: return 0
        r += self.size
        for i in range(self.log, 0, -1): self.__push(r >> i)
        sm = self.e()
        while True:
            r -= 1
            while r > 1 and r % 2: r >>= 1
            if not g(self.op(self.d[r], sm)):
                while r < self.size:
                    self.__push(r)
                    r = 2 * r + 1
                    if g(self.op(self.d[r], sm)):
                        sm = self.op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.d[r], sm)
            if (r & -r) == r: break
        return 0

    # private
    def __update(self, k: int): self.d[k] = self.op(self.d[k * 2], self.d[k * 2 + 1])

    def __all_apply(self, k: int, f):
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size: self.lz[k] = self.composition(f, self.lz[k])

    def __push(self, k: int):
        self.__all_apply(2 * k, self.lz[k])
        self.__all_apply(2 * k + 1, self.lz[k])
        self.lz[k] = self.id()

def ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n: x += 1
    return x

class S:
    def __init__(self, a: int, sz: int, rp: int):
        self.a = a; self.sz = sz; self.rp = rp

p = 998244353
def op(l, r):
    l1, l2 = l >> 32, l & ((1 << 32) - 1)
    r1, r2 = r >> 32, r & ((1 << 32) - 1)
    return (((l1 + r1) % p) << 32) + (l2 + r2) % p
def e(): return 0
def mapping(l, r):
    l1, l2 = l >> 32, l & ((1 << 32) - 1)
    r1, r2 = r >> 32, r & ((1 << 32) - 1)
    if l1 == 0: return r
    return (((r2 * l1) % p) << 32) + r2

def composition(l, r):
    l1, l2 = l >> 32, l & ((1 << 32) - 1)
    r1, r2 = r >> 32, r & ((1 << 32) - 1)
    if l1 == 0: return r
    return l
def id(): return 0

def Main():
    n, q = read_ints()
    a = [(pow(10, n - i - 1, p) << 32) + pow(10, n - i - 1, p) for i in range(n)]
    seg = lazy_segtree(op, e, mapping, composition, id, a)
    for i in range(q):
        l, r, d = read_ints()
        seg.apply(~-l, r, (d << 32) + i)
        print(seg.all_prod() >> 32)

if __name__ == '__main__':
    Main()
